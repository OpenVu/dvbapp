from enigma import eDVBFrontendParametersSatellite, eDVBFrontendParametersCable, eDVBFrontendParametersTerrestrial
from Components.NimManager import nimmanager

def ConvertToHumanReadable(tp, type = None):
	ret = { }
	if type is None:
		type = tp.get("tuner_type", "None")
	if type == "DVB-S":
		ret["tuner_type"] = _("Satellite")
		ret["inversion"] = {
			eDVBFrontendParametersSatellite.Inversion_Unknown : _("Auto"),
			eDVBFrontendParametersSatellite.Inversion_On : _("On"),
			eDVBFrontendParametersSatellite.Inversion_Off : _("Off")}[tp["inversion"]]
		ret["fec_inner"] = {
			eDVBFrontendParametersSatellite.FEC_None : _("None"),
			eDVBFrontendParametersSatellite.FEC_Auto : _("Auto"),
			eDVBFrontendParametersSatellite.FEC_1_2 : "1/2",
			eDVBFrontendParametersSatellite.FEC_2_3 : "2/3",
			eDVBFrontendParametersSatellite.FEC_3_4 : "3/4",
			eDVBFrontendParametersSatellite.FEC_5_6 : "5/6",
			eDVBFrontendParametersSatellite.FEC_7_8 : "7/8",
			eDVBFrontendParametersSatellite.FEC_3_5 : "3/5",
			eDVBFrontendParametersSatellite.FEC_4_5 : "4/5",
			eDVBFrontendParametersSatellite.FEC_8_9 : "8/9",
			eDVBFrontendParametersSatellite.FEC_9_10 : "9/10",
			eDVBFrontendParametersSatellite.FEC_13_45 : "13/45",
			eDVBFrontendParametersSatellite.FEC_9_20 : "9/20",
			eDVBFrontendParametersSatellite.FEC_11_20 : "11/20",
			eDVBFrontendParametersSatellite.FEC_23_36 : "23/36",
			eDVBFrontendParametersSatellite.FEC_25_36 : "25/36",
			eDVBFrontendParametersSatellite.FEC_13_18 : "13/18",
			eDVBFrontendParametersSatellite.FEC_26_45 : "26/45",
			eDVBFrontendParametersSatellite.FEC_28_45 : "28/45",
			eDVBFrontendParametersSatellite.FEC_7_9 : "7/9",
			eDVBFrontendParametersSatellite.FEC_77_90 : "77/90",
			eDVBFrontendParametersSatellite.FEC_32_45 : "32/45",
			eDVBFrontendParametersSatellite.FEC_11_15 : "11/15",
			eDVBFrontendParametersSatellite.FEC_1_2_L : "1/2-L",
			eDVBFrontendParametersSatellite.FEC_8_15_L : "8/15-L",
			eDVBFrontendParametersSatellite.FEC_3_5_L : "3/5-L",
			eDVBFrontendParametersSatellite.FEC_2_3_L : "2/3-L",
			eDVBFrontendParametersSatellite.FEC_5_9_L : "5/9-L",
			eDVBFrontendParametersSatellite.FEC_26_45_L : "26/45-L"}[tp["fec_inner"]]
		ret["modulation"] = {
			eDVBFrontendParametersSatellite.Modulation_Auto : _("Auto"),
			eDVBFrontendParametersSatellite.Modulation_QPSK : "QPSK",
			eDVBFrontendParametersSatellite.Modulation_QAM16 : "QAM16",
			eDVBFrontendParametersSatellite.Modulation_8PSK : "8PSK",
			eDVBFrontendParametersSatellite.Modulation_16APSK : "16APSK",
			eDVBFrontendParametersSatellite.Modulation_32APSK : "32APSK",
			eDVBFrontendParametersSatellite.Modulation_8APSK : "8APSK",
			}[tp["modulation"]]
		ret["orbital_position"] = nimmanager.getSatName(int(tp["orbital_position"]))
		ret["polarization"] = {
			eDVBFrontendParametersSatellite.Polarisation_Horizontal : _("Horizontal"),
			eDVBFrontendParametersSatellite.Polarisation_Vertical : _("Vertical"),
			eDVBFrontendParametersSatellite.Polarisation_CircularLeft : _("Circular left"),
			eDVBFrontendParametersSatellite.Polarisation_CircularRight : _("Circular right")}[tp["polarization"]]
		ret["system"] = {
			eDVBFrontendParametersSatellite.System_DVB_S : "DVB-S",
			eDVBFrontendParametersSatellite.System_DVB_S2 : "DVB-S2",
			eDVBFrontendParametersSatellite.System_DVB_S2X : "DVB-S2X"}[tp["system"]]
		if ret["system"] in ("DVB-S2", "DVB-S2X"):
			ret["rolloff"] = {
				eDVBFrontendParametersSatellite.RollOff_alpha_0_35 : "0.35",
				eDVBFrontendParametersSatellite.RollOff_alpha_0_25 : "0.25",
				eDVBFrontendParametersSatellite.RollOff_alpha_0_20 : "0.20"}.get(tp.get("rolloff", "auto"))
			ret["pilot"] = {
				eDVBFrontendParametersSatellite.Pilot_Unknown : _("Auto"),
				eDVBFrontendParametersSatellite.Pilot_On : _("On"),
				eDVBFrontendParametersSatellite.Pilot_Off : _("Off")}[tp["pilot"]]
			ret["pls_mode"] = {
				eDVBFrontendParametersSatellite.PLS_Root : _("Root"),
				eDVBFrontendParametersSatellite.PLS_Gold : _("Gold"),
				eDVBFrontendParametersSatellite.PLS_Combo : _("Combo"),
				eDVBFrontendParametersSatellite.PLS_Unknown : _("Auto")}.get(tp.get("pls_mode"))
			#ret["is_id"] = tp.get("is_id")
			#ret["pls_code"] = tp.get("pls_code")
		else:
			ret["pls_mode"] = None
			ret["is_id"] = None
			ret["pls_code"] = None
	elif type == "DVB-C":
		ret["tuner_type"] = _("Cable")
		ret["modulation"] = {
			eDVBFrontendParametersCable.Modulation_Auto: _("Auto"),
			eDVBFrontendParametersCable.Modulation_QAM16 : "QAM16",
			eDVBFrontendParametersCable.Modulation_QAM32 : "QAM32",
			eDVBFrontendParametersCable.Modulation_QAM64 : "QAM64",
			eDVBFrontendParametersCable.Modulation_QAM128 : "QAM128",
			eDVBFrontendParametersCable.Modulation_QAM256 : "QAM256"}[tp["modulation"]]
		ret["inversion"] = {
			eDVBFrontendParametersCable.Inversion_Unknown : _("Auto"),
			eDVBFrontendParametersCable.Inversion_On : _("On"),
			eDVBFrontendParametersCable.Inversion_Off : _("Off")}[tp["inversion"]]
		ret["fec_inner"] = {
			eDVBFrontendParametersCable.FEC_None : _("None"),
			eDVBFrontendParametersCable.FEC_Auto : _("Auto"),
			eDVBFrontendParametersCable.FEC_1_2 : "1/2",
			eDVBFrontendParametersCable.FEC_2_3 : "2/3",
			eDVBFrontendParametersCable.FEC_3_4 : "3/4",
			eDVBFrontendParametersCable.FEC_5_6 : "5/6",
			eDVBFrontendParametersCable.FEC_7_8 : "7/8",
			eDVBFrontendParametersCable.FEC_8_9 : "8/9"}[tp["fec_inner"]]
	elif type == "DVB-T":
		ret["tuner_type"] = _("Terrestrial")
		ret["bandwidth"] = {
			eDVBFrontendParametersTerrestrial.Bandwidth_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.Bandwidth_10MHz : "10 MHz",
			eDVBFrontendParametersTerrestrial.Bandwidth_8MHz : "8 MHz",
			eDVBFrontendParametersTerrestrial.Bandwidth_7MHz : "7 MHz",
			eDVBFrontendParametersTerrestrial.Bandwidth_6MHz : "6 MHz",
			eDVBFrontendParametersTerrestrial.Bandwidth_5MHz : "5 MHz",
			eDVBFrontendParametersTerrestrial.Bandwidth_1_712MHz : "1.172 MHz"}.get(tp.get("bandwidth", " "))
		ret["code_rate_lp"] = {
			eDVBFrontendParametersTerrestrial.FEC_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.FEC_1_2 : "1/2",
			eDVBFrontendParametersTerrestrial.FEC_2_3 : "2/3",
			eDVBFrontendParametersTerrestrial.FEC_3_4 : "3/4",
			eDVBFrontendParametersTerrestrial.FEC_4_5 : "4/5",
			eDVBFrontendParametersTerrestrial.FEC_5_6 : "5/6",
			eDVBFrontendParametersTerrestrial.FEC_6_7 : "6/7",
			eDVBFrontendParametersTerrestrial.FEC_7_8 : "7/8",
			eDVBFrontendParametersTerrestrial.FEC_8_9 : "8/9"}.get(tp.get("code_rate_lp", " "))
		ret["code_rate_hp"] = {
			eDVBFrontendParametersTerrestrial.FEC_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.FEC_1_2 : "1/2",
			eDVBFrontendParametersTerrestrial.FEC_2_3 : "2/3",
			eDVBFrontendParametersTerrestrial.FEC_3_4 : "3/4",
			eDVBFrontendParametersTerrestrial.FEC_4_5 : "4/5",
			eDVBFrontendParametersTerrestrial.FEC_5_6 : "5/6",
			eDVBFrontendParametersTerrestrial.FEC_6_7 : "6/7",
			eDVBFrontendParametersTerrestrial.FEC_7_8 : "7/8",
			eDVBFrontendParametersTerrestrial.FEC_8_9 : "8/9"}.get(tp.get("code_rate_hp", " "))
		ret["constellation"] = {
			eDVBFrontendParametersTerrestrial.Modulation_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.Modulation_QPSK : "QPSK",
			eDVBFrontendParametersTerrestrial.Modulation_QAM16 : "QAM16",
			eDVBFrontendParametersTerrestrial.Modulation_QAM64 : "QAM64",
			eDVBFrontendParametersTerrestrial.Modulation_QAM256 : "QAM256"}.get(tp.get("constellation", " "))
		ret["transmission_mode"] = {
			eDVBFrontendParametersTerrestrial.TransmissionMode_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.TransmissionMode_1k : "1k",
			eDVBFrontendParametersTerrestrial.TransmissionMode_2k : "2k",
			eDVBFrontendParametersTerrestrial.TransmissionMode_4k : "4k",
			eDVBFrontendParametersTerrestrial.TransmissionMode_8k : "8k",
			eDVBFrontendParametersTerrestrial.TransmissionMode_16k : "16k",
			eDVBFrontendParametersTerrestrial.TransmissionMode_32k : "32k"}.get(tp.get("transmission_mode", " "))
		ret["guard_interval"] = {
			eDVBFrontendParametersTerrestrial.GuardInterval_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.GuardInterval_19_256 : "19/256",
			eDVBFrontendParametersTerrestrial.GuardInterval_19_128 : "19/128",
			eDVBFrontendParametersTerrestrial.GuardInterval_1_128 : "1/128",
			eDVBFrontendParametersTerrestrial.GuardInterval_1_32 : "1/32",
			eDVBFrontendParametersTerrestrial.GuardInterval_1_16 : "1/16",
			eDVBFrontendParametersTerrestrial.GuardInterval_1_8 : "1/8",
			eDVBFrontendParametersTerrestrial.GuardInterval_1_4 : "1/4"}.get(tp.get("guard_interval", " "))
		ret["hierarchy_information"] = {
			eDVBFrontendParametersTerrestrial.Hierarchy_Auto : _("Auto"),
			eDVBFrontendParametersTerrestrial.Hierarchy_None : _("None"),
			eDVBFrontendParametersTerrestrial.Hierarchy_1 : "1",
			eDVBFrontendParametersTerrestrial.Hierarchy_2 : "2",
			eDVBFrontendParametersTerrestrial.Hierarchy_4 : "4"}.get(tp.get("hierarchy_information", " "))
		ret["inversion"] = {
			eDVBFrontendParametersTerrestrial.Inversion_Unknown : _("Auto"),
			eDVBFrontendParametersTerrestrial.Inversion_On : _("On"),
			eDVBFrontendParametersTerrestrial.Inversion_Off : _("Off")}.get(tp.get("inversion", " "))
		ret["system"] = {
			eDVBFrontendParametersTerrestrial.System_DVB_T : "DVB-T",
			eDVBFrontendParametersTerrestrial.System_DVB_T2 : "DVB-T2"}[tp.get("system")]
	else:
		print "ConvertToHumanReadable: no or unknown type in tpdata dict!"
	for x in tp.keys():
		if not ret.has_key(x):
			ret[x] = tp[x]
	return ret
