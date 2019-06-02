#
# PySNMP MIB module IBM2260-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM2260-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, enterprises, NotificationType, ObjectIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, IpAddress, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "enterprises", "NotificationType", "ObjectIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "IpAddress", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500PCTStationProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500PSTStationProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500PPCTIBM2260PortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20), )
if mibBuilder.loadTexts: cdx6500PPCTIBM2260PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTIBM2260PortTable.setDescription('A list of IBM2260 Port configuration entries.')
cdx6500PPCTIBM2260PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1), ).setIndexNames((0, "IBM2260-OPT-MIB", "cdx6500IBM2260CfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTIBM2260PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTIBM2260PortEntry.setDescription('An IBM2260 Configuration Table entry. Each entry contains the configuration parameters for a single IBM2260 port. ')
cdx6500IBM2260CfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortNumber.setDescription('The port number corresponding to this port.')
cdx6500IBM2260CfgPadType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tpad", 1), ("hpad", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgPadType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgPadType.setDescription('Indicates whether the port is functioning as a Terminal PAD (TPAD) or a Host PAD (HPAD).')
cdx6500IBM2260CfgPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 8, 13, 14, 15, 16, 99))).clone(namedValues=NamedValues(("speed1200", 4), ("speed1800", 8), ("speed2400", 13), ("speed4800", 14), ("speed9600", 15), ("speed19200", 16), ("speed7200", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortSpeed.setDescription('This is the speed of the port in bits per second, when using internal clocking.')
cdx6500IBM2260CfgConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 16))).clone(namedValues=NamedValues(("simp", 1), ("simpa", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgConnType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgConnType.setDescription('Specify the control signal handshake required for a connection to be made to this port: simp - simple, no control signals required. simpa - CTS follows RTS, but no control signals required.')
cdx6500IBM2260CfgNumDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgNumDevice.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgNumDevice.setDescription('Specifies the number of IBM2260 stations on this line.')
cdx6500IBM2260CfgServiceTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgServiceTimer.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgServiceTimer.setDescription('The Service Timer specifies the interval of time in seconds between periodic servicing. Such servicing includes intervals between attempts to establish network connections, intervals between attempts in TPAD to poll terminals that previously failed to respond, and in HPAD this timer is also used to detect host inactivity (i.e. when the host stops polling the station(s)).')
cdx6500IBM2260CfgThreshCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgThreshCtr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgThreshCtr.setDescription('Indicates number of consecutive errors that can occur before a station is considered down.')
cdx6500IBM2260CfgRespTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgRespTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgRespTimeout.setDescription("Specifies the amount of time in msec the PAD allows a terminal, printer or host to respond. As a result, the TPAD may re-transmit the previous message or abort the current procedure. The HPAD aborts the current procedure as though EOT was received, allowing this HPAD station to disconnect it's SVC if the host malfunctions. An HPAD with a response timeout shorter than the hosts ability to respond may result in Inbound Errors.")
cdx6500IBM2260CfgPortSubAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortSubAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortSubAddr.setDescription('Calls addressed to this node and with this subaddress will be routed to this port.')
cdx6500IBM2260CfgPortOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortOpt.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgPortOpt.setDescription('Select options on this IBM2260 port as follows: NONE - No option specified ORG - Originate calls from this port ACK - DSP End-to-End Acknowledgements are to be used Any combination of above specified by summing (e.g. ORG+ACK).')
cdx6500IBM2260CfgRestConnDest = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgRestConnDest.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgRestConnDest.setDescription('All calls originating from this port will be routed to the destination specified in this parameter, irrespective of route selection table entries. For example, to route calls to port 1, use P1. To route calls to port 2, station 4, use P2S4. Blank this field to disable this function.')
cdx6500IBM2260CfgBillRec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgBillRec.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgBillRec.setDescription('This controls whether billing (accounting) records will be created for calls on this port.')
cdx6500IBM2260CfgElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgElectricalInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgElectricalInterfaceType.setDescription('Specify the Electrical Interface Type: V.24 - V.24 Electrical Interface Type V.35 - V.35 Electrical Interface Type V.36 - V.36 Electrical Interface Type X.21 - X.21 Electrical Interface Type Note: Changing this parameter requires manual settings on SWITCH1: Interface SW1-1 SW1-2 SW1-3 SW1-4 SW1-5 SW1-6 SW1-7 SW1-8 V.24 ON ON ON ON ON OFF OFF OFF V.35,V.36,X.21 OFF OFF OFF OFF OFF ON ON ON')
cdx6500IBM2260CfgV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgV24ElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgV24ElectricalInterfaceOption.setDescription('Specify the Pin 22 option: RI - V.24 uses Pin 22 for Ring Indicator output signal TM - V.24 uses Pin 22 for Test Mode input signal')
cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption.setDescription('Specify the cable type: NONE - V.35/V.36/X.21 DCE with straight through cable XOVER - V.35/V.36/X.21 DCE with crossover adapter cable')
cdx6500PPSTIBM2260PortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19), )
if mibBuilder.loadTexts: cdx6500PPSTIBM2260PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPSTIBM2260PortTable.setDescription('A list of IBM2260 Port statistics.')
cdx6500PPSTIBM2260PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1), ).setIndexNames((0, "IBM2260-OPT-MIB", "cdx6500IBM2260StatPortNumber"))
if mibBuilder.loadTexts: cdx6500PPSTIBM2260PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPSTIBM2260PortEntry.setDescription('An IBM2260 Statistics Table entry. Each entry contains the statistics for a single IBM2260 port. ')
cdx6500IBM2260StatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortNumber.setDescription('Physical port number')
cdx6500IBM2260StatPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortStatus.setDescription('Operational Status of the port. The different operational statuses are: UP : At least 1 station is responding to polls. DOWN : None of the stations are responding to polls. DISABLED : The port is disabled by the user.')
cdx6500IBM2260StatPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortState.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortState.setDescription('Current State of this port.')
cdx6500IBM2260StatPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("speed1200", 1), ("speed1800", 2), ("speed2400", 3), ("speed4800", 4), ("speed7200", 5), ("speed9600", 6), ("speed19200", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortSpeed.setDescription('The measured port speed in bits per second.')
cdx6500IBM2260StatPortUtilin = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortUtilin.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortUtilin.setDescription("The amount of the port's bandwidth that is being utilized; because IBM2260 is a half-duplex protocol the utilization is calculated as the sum of the receive and transmit utilization.")
cdx6500IBM2260StatPortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPortUtilOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPortUtilOut.setDescription("The amount of the port's bandwidth that is being utilized; because IBM2260 is a half-duplex protocol the utilization is calculated as the sum of the receive and transmit utilization.")
cdx6500IBM2260StatParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatParityErrors.setDescription('The number of character parity errors counted by the I/O driver.')
cdx6500IBM2260StatOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatOverrunErrors.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatOverrunErrors.setDescription('The number of received character overruns counted by the I/O driver.')
cdx6500IBM2260StatFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatFramingErrors.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatFramingErrors.setDescription('The number of asynchronous chracters received which violated the character framing of start and stop bits. Note, this statistic is only valid if the port is configured for ASYNC line interface.')
cdx6500IBM2260StatBCCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatBCCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatBCCErrors.setDescription('The number of BCC errors counted by the I/O driver.')
cdx6500IBM2260StatNoResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatNoResponse.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatNoResponse.setDescription('The number of times the response timer has expired.')
cdx6500IBM2260StatCharInTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatCharInTotal.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatCharInTotal.setDescription('Total number of chracters received to present.')
cdx6500IBM2260StatCharOutTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatCharOutTotal.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatCharOutTotal.setDescription('Total number of chracters transmitted to present.')
cdx6500IBM2260StatCharInSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatCharInSecond.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatCharInSecond.setDescription('Average number of characters received to present.')
cdx6500IBM2260StatCharOutSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatCharOutSecond.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatCharOutSecond.setDescription('Average number of characters transmitted to present.')
cdx6500IBM2260StatPosAckIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPosAckIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPosAckIn.setDescription('Number of ACKs received.')
cdx6500IBM2260StatPosAckOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatPosAckOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatPosAckOut.setDescription('Number of ACKs transmitted.')
cdx6500IBM2260StatNegAckIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatNegAckIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatNegAckIn.setDescription('Number of NAKs received.')
cdx6500IBM2260StatNegAckOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatNegAckOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatNegAckOut.setDescription('Number of NAKs transmitted.')
cdx6500IBM2260StatMsgRetran = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260StatMsgRetran.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260StatMsgRetran.setDescription('Number of messages retransmitted due to NAKs or timeouts to present.')
cdx6500SPCTIBM2260StationTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6), )
if mibBuilder.loadTexts: cdx6500SPCTIBM2260StationTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500SPCTIBM2260StationTable.setDescription('All of the configuration parameters relevant to the IBM2260 Station table.')
cdx6500SPCTIBM2260StationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1), ).setIndexNames((0, "IBM2260-OPT-MIB", "cdx6500IBM2260sCfgPortNum"), (0, "IBM2260-OPT-MIB", "cdx6500IBM2260sCfgStationNum"))
if mibBuilder.loadTexts: cdx6500SPCTIBM2260StationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500SPCTIBM2260StationEntry.setDescription('A row of IBM2260 station configuration parameters.')
cdx6500IBM2260sCfgPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sCfgPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sCfgPortNum.setDescription('Port number.')
cdx6500IBM2260sCfgStationNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sCfgStationNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sCfgStationNum.setDescription('Station number.')
cdx6500IBM2260sType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("single", 1), ("group", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sType.setDescription("single - configures a single station addressable by the ADDR1-ADDR2 address pair. group - configures a group of stations addressable by the ADDR1 address character, but ADDR2 is assumed to be 40H, 41H, 42H and 43H. This type is intended for support of DataTroll devices. NOTE: `group' Station should not be used when the BSC3270-IBM2260 protocol Interoperation is being used.")
cdx6500IBM2260sStationAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sStationAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sStationAddr1.setDescription("This is the first byte of this Station's address. The Station address consists of two hexadecimal digits. The valid range for a digit is: 20-7F;")
cdx6500IBM2260sStationAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sStationAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sStationAddr2.setDescription("This is the second byte of this Station's address. The Station address consists of two hexadecimal digits. The valid range for a digit is: 20-7F")
cdx6500IBM2260sCallMnem = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sCallMnem.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sCallMnem.setDescription('This mnemonic name is used if this port is configured for originating connection requests.')
cdx6500IBM2260sStationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500IBM2260sStationEnable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500IBM2260sStationEnable.setDescription('This parameter is used to disable/enable a station.')
mibBuilder.exportSymbols("IBM2260-OPT-MIB", cdx6500PPCTIBM2260PortTable=cdx6500PPCTIBM2260PortTable, cdx6500IBM2260CfgServiceTimer=cdx6500IBM2260CfgServiceTimer, cdx6500IBM2260StatBCCErrors=cdx6500IBM2260StatBCCErrors, cdx6500IBM2260CfgPortSpeed=cdx6500IBM2260CfgPortSpeed, cdx6500IBM2260CfgV24ElectricalInterfaceOption=cdx6500IBM2260CfgV24ElectricalInterfaceOption, cdx6500PPSTIBM2260PortEntry=cdx6500PPSTIBM2260PortEntry, cdx6500IBM2260CfgPortNumber=cdx6500IBM2260CfgPortNumber, cdx6500IBM2260StatOverrunErrors=cdx6500IBM2260StatOverrunErrors, cdx6500IBM2260StatNegAckIn=cdx6500IBM2260StatNegAckIn, cdx6500Configuration=cdx6500Configuration, cdx6500Controls=cdx6500Controls, cdx6500IBM2260StatPortUtilin=cdx6500IBM2260StatPortUtilin, cdx6500IBM2260StatCharOutTotal=cdx6500IBM2260StatCharOutTotal, cdx6500IBM2260sCfgStationNum=cdx6500IBM2260sCfgStationNum, cdx6500IBM2260StatFramingErrors=cdx6500IBM2260StatFramingErrors, cdx6500IBM2260sStationEnable=cdx6500IBM2260sStationEnable, cdx6500PPCTIBM2260PortEntry=cdx6500PPCTIBM2260PortEntry, cdx6500IBM2260sType=cdx6500IBM2260sType, cdx6500IBM2260CfgPortSubAddr=cdx6500IBM2260CfgPortSubAddr, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500IBM2260CfgPortOpt=cdx6500IBM2260CfgPortOpt, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500IBM2260CfgRestConnDest=cdx6500IBM2260CfgRestConnDest, cdx6500IBM2260StatPosAckIn=cdx6500IBM2260StatPosAckIn, cdx6500SPCTIBM2260StationTable=cdx6500SPCTIBM2260StationTable, cdx6500IBM2260StatCharInTotal=cdx6500IBM2260StatCharInTotal, cdx6500IBM2260StatPortStatus=cdx6500IBM2260StatPortStatus, cdx6500IBM2260sStationAddr2=cdx6500IBM2260sStationAddr2, cdx6500Statistics=cdx6500Statistics, cdx6500IBM2260CfgElectricalInterfaceType=cdx6500IBM2260CfgElectricalInterfaceType, cdx6500IBM2260CfgConnType=cdx6500IBM2260CfgConnType, cdx6500PPSTIBM2260PortTable=cdx6500PPSTIBM2260PortTable, cdx6500IBM2260CfgNumDevice=cdx6500IBM2260CfgNumDevice, cdx6500IBM2260sCallMnem=cdx6500IBM2260sCallMnem, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500IBM2260StatCharOutSecond=cdx6500IBM2260StatCharOutSecond, cdx6500IBM2260StatNoResponse=cdx6500IBM2260StatNoResponse, cdx6500IBM2260CfgBillRec=cdx6500IBM2260CfgBillRec, cdx6500IBM2260StatPortState=cdx6500IBM2260StatPortState, cdx6500IBM2260sStationAddr1=cdx6500IBM2260sStationAddr1, cdx6500IBM2260StatPortNumber=cdx6500IBM2260StatPortNumber, cdx6500IBM2260StatParityErrors=cdx6500IBM2260StatParityErrors, cdx6500SPCTIBM2260StationEntry=cdx6500SPCTIBM2260StationEntry, cdx6500IBM2260StatPortSpeed=cdx6500IBM2260StatPortSpeed, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500IBM2260sCfgPortNum=cdx6500IBM2260sCfgPortNum, cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption=cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption, codex=codex, cdx6500IBM2260StatPosAckOut=cdx6500IBM2260StatPosAckOut, cdx6500IBM2260StatMsgRetran=cdx6500IBM2260StatMsgRetran, DisplayString=DisplayString, cdxProductSpecific=cdxProductSpecific, cdx6500IBM2260CfgPadType=cdx6500IBM2260CfgPadType, cdx6500IBM2260CfgRespTimeout=cdx6500IBM2260CfgRespTimeout, cdx6500=cdx6500, cdx6500IBM2260CfgThreshCtr=cdx6500IBM2260CfgThreshCtr, cdx6500IBM2260StatNegAckOut=cdx6500IBM2260StatNegAckOut, cdx6500IBM2260StatPortUtilOut=cdx6500IBM2260StatPortUtilOut, cdx6500PCTStationProtocolGroup=cdx6500PCTStationProtocolGroup, cdx6500IBM2260StatCharInSecond=cdx6500IBM2260StatCharInSecond, cdx6500PSTStationProtocolGroup=cdx6500PSTStationProtocolGroup)