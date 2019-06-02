#
# PySNMP MIB module DELL-NETWORKING-IF-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-IF-EXTENSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:38:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Gauge32, Bits, Integer32, Counter64, iso, Counter32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Bits", "Integer32", "Counter64", "iso", "Counter32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "TruthValue")
dellNetIfExtensionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 11))
dellNetIfExtensionMib.setRevisions(('2014-08-12 12:00', '2012-03-06 12:00', '2010-08-11 12:00', '2010-08-10 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dellNetIfExtensionMib.setRevisionsDescriptions(('Added dellNetIfPortListBitPos.Removed dellNetIfDhcpAdminStatus and dellNetIfDhcpOperStatus.', 'Added DHCP Client attributes.', 'Add dellNetIfOutThrottles.', 'Initial version of this mib module.',))
if mibBuilder.loadTexts: dellNetIfExtensionMib.setLastUpdated('201203061200Z')
if mibBuilder.loadTexts: dellNetIfExtensionMib.setOrganization('Dell Inc')
if mibBuilder.loadTexts: dellNetIfExtensionMib.setContactInfo('http://www.dell.com/support')
if mibBuilder.loadTexts: dellNetIfExtensionMib.setDescription('Dell Networking OS IF Extenstion MIB. ')
dellNetIfExtensionMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1))
dellNetIfExtensionParams = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1))
dellNetIfExtensionStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2))
dellNetIfTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1), )
if mibBuilder.loadTexts: dellNetIfTable.setStatus('current')
if mibBuilder.loadTexts: dellNetIfTable.setDescription('Dell Networking OS Extension ifTable contains generic interface parameters.')
dellNetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dellNetIfEntry.setStatus('current')
if mibBuilder.loadTexts: dellNetIfEntry.setDescription(' A row defintion of Dell Networking OS Interface Extension parameters.')
dellNetIfIpMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(594, 9252))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfIpMtu.setStatus('current')
if mibBuilder.loadTexts: dellNetIfIpMtu.setDescription('The IP (Internet Protocol), Maximum Transmission Unit value.')
dellNetIfDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfDuplexMode.setStatus('current')
if mibBuilder.loadTexts: dellNetIfDuplexMode.setDescription('Duplex mode of the interface. This will be read-write only for s60')
dellNetIfQueueingStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfQueueingStrategy.setStatus('current')
if mibBuilder.loadTexts: dellNetIfQueueingStrategy.setDescription('Queueing strategy used for packets.')
dellNetIfRxFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfRxFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: dellNetIfRxFlowCtrl.setDescription('Flow control receive. This will be read-write only for s60')
dellNetIfTxFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfTxFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: dellNetIfTxFlowCtrl.setDescription('Flow Control transmit.This will be read-only only for s60')
dellNetIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 241))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfDescr.setStatus('current')
if mibBuilder.loadTexts: dellNetIfDescr.setDescription('A textual string containing information about the interface. This will be read-write only for s60')
dellNetIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: dellNetIfAdminStatus.setDescription('A admin status of any interface. This will be read-write only for s60')
dellNetIfRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 299))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfRateInterval.setStatus('current')
if mibBuilder.loadTexts: dellNetIfRateInterval.setDescription('The rate info interval for the interface. This will be read-write only for s60')
dellNetIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 100, 1000))).clone(namedValues=NamedValues(("auto", 1), ("tenMbps", 10), ("hundredMbps", 100), ("thousandMbps", 1000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellNetIfSpeed.setStatus('current')
if mibBuilder.loadTexts: dellNetIfSpeed.setDescription("The interface's current bandwidth in bits per second. This will be read-write only for s60")
dellNetIfPortListBitPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfPortListBitPos.setStatus('current')
if mibBuilder.loadTexts: dellNetIfPortListBitPos.setDescription('This is used for identifying the bit position in PortList Object for a given interface.')
dellNetIfStaticsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1), )
if mibBuilder.loadTexts: dellNetIfStaticsTable.setStatus('current')
if mibBuilder.loadTexts: dellNetIfStaticsTable.setDescription('The statistcs information of the interfaces for performance monitoring.')
dellNetIfStaticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dellNetIfStaticsEntry.setStatus('current')
if mibBuilder.loadTexts: dellNetIfStaticsEntry.setDescription('A row defintion of Dell Networking OS Extension interface statistics.')
dellNetIfInVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInVlanPkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInVlanPkts.setDescription('The total number of valid VLAN Tagged frames received.')
dellNetIfIn64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfIn64BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfIn64BytePkts.setDescription('The total number of frames (including bad frames) received that were 64 octets in length (excluding framing bits but in-cluding FCS octets).')
dellNetifIn65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetifIn65To127BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetifIn65To127BytePkts.setDescription('The total number of frames (including bad frames) received that were between 65 and 127 octets in length inclusive (ex-cluding framing bits but including FCS octets).')
dellNetIfIn128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfIn128To255BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfIn128To255BytePkts.setDescription('The total number of frames (including bad frames) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).')
dellNetIfIn256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfIn256To511BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfIn256To511BytePkts.setDescription('The total number of frames (including bad frames) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).')
dellNetIfIn512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfIn512To1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfIn512To1023BytePkts.setDescription('The total number of frames (including bad frames) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).')
dellNetIfInOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInOver1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInOver1023BytePkts.setDescription('The total number of frames received that were longer than 1023 (1025 Bytes in case of VLAN Tag) octets (excluding framing bits, but including FCS octets) and were otherwise well formed. This counter is not incremented for too long frames.')
dellNetIfInThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInThrottles.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInThrottles.setDescription('This counter is incremented when a valid frame with a length or type field value equal to 0x8808 (Control Frame) is re-ceived.')
dellNetIfInRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInRunts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInRunts.setDescription('The total number of frames received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.')
dellNetIfInGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInGiants.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInGiants.setDescription('The total number of frames received that were longer than 1518 (1522 Bytes in case of VLAN Tag) octets (excluding framing bits, but including FCS octets) and were otherwise well formed. This counter is not incremented for too long frames.')
dellNetIfInCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInCRC.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInCRC.setDescription('The total number of frames received that had a length (ex-cluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad CRC.')
dellNetIfInOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInOverruns.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInOverruns.setDescription('The total number of frames dropped because of buffer issue.')
dellNetIfOutVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutVlanPkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutVlanPkts.setDescription('The Number of Good VLAN Tagged Frames sent successfully.')
dellNetIfOutUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutUnderruns.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutUnderruns.setDescription('The total number of frames dropped because of buffer underrun.')
dellNetIfOutUnicasts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutUnicasts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutUnicasts.setDescription('The Number of Good Unicast Frames sent successfully.')
dellNetIfOutCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutCollisions.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutCollisions.setDescription('A count of the frames that due to excessive or late collisions are not transmitted successfully.')
dellNetIfOutWredDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutWredDrops.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutWredDrops.setDescription('A count of the frames that are dropped using WRED policy because of to excessive traffic.')
dellNetIfOut64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOut64BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOut64BytePkts.setDescription('The Number of Good Frames sent successfully whose size was 64 Bytes.')
dellNetIfOut65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOut65To127BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOut65To127BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 65 to 127 Bytes.')
dellNetIfOut128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOut128To255BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOut128To255BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 128 to 255 Bytes.')
dellNetIfOut256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOut256To511BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOut256To511BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 256 to 511 Bytes.')
dellNetIfOut512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOut512To1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOut512To1023BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 512 to 1023 Bytes.')
dellNetIfOutOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutOver1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutOver1023BytePkts.setDescription('The Number of Good Frames sent successfully whose size was greater than 1023 Bytes.')
dellNetIfOutThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutThrottles.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutThrottles.setDescription('This counter is incremented when a valid frame with a length or type field value equal to 0x8808 (Control Frame) is sent.')
dellNetIfLastDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 25), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfLastDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: dellNetIfLastDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which this interface's counters suffered a discontinuity via a reset. If no such discontinuities have occurred since the last reinitialization of the local management subsystem, then this object contains a zero value.")
dellNetIfInCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfInCentRate.setStatus('current')
if mibBuilder.loadTexts: dellNetIfInCentRate.setDescription('This is the ingress rate in percentage. This is an integer value which can go from 0 to 100.')
dellNetIfOutCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIfOutCentRate.setStatus('current')
if mibBuilder.loadTexts: dellNetIfOutCentRate.setDescription('This is the egress rate in percentage. This is an integer value which can go from 0 to 100.')
dellNetIfExtensionMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2))
dellNetIfExtensionMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1))
dellNetIfExtensionMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2))
dellNetIfExtensionMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1, 1)).setObjects(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfParamsGroup"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIfExtensionMibCompliance = dellNetIfExtensionMibCompliance.setStatus('current')
if mibBuilder.loadTexts: dellNetIfExtensionMibCompliance.setDescription('The compliance statement for Dell Networking OS IF Extension MIB.')
dellNetIfParamsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 1)).setObjects(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIpMtu"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDuplexMode"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfQueueingStrategy"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRxFlowCtrl"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTxFlowCtrl"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDescr"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAdminStatus"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRateInterval"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfSpeed"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfPortListBitPos"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIfParamsGroup = dellNetIfParamsGroup.setStatus('current')
if mibBuilder.loadTexts: dellNetIfParamsGroup.setDescription('A collection of objects providing the Dell Networking OS IF Extenstion parameters.')
dellNetIfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 2)).setObjects(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInVlanPkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn64BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetifIn65To127BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn128To255BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn256To511BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn512To1023BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOver1023BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInThrottles"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInRunts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInGiants"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCRC"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOverruns"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutVlanPkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnderruns"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnicasts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCollisions"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutWredDrops"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut64BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut65To127BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut128To255BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut256To511BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut512To1023BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutOver1023BytePkts"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutThrottles"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfLastDiscontinuityTime"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCentRate"), ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCentRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIfStatsGroup = dellNetIfStatsGroup.setStatus('current')
if mibBuilder.loadTexts: dellNetIfStatsGroup.setDescription('A collection of objects providing the interface statistics.')
mibBuilder.exportSymbols("DELL-NETWORKING-IF-EXTENSION-MIB", dellNetIfInCRC=dellNetIfInCRC, dellNetIfExtensionMibConformance=dellNetIfExtensionMibConformance, dellNetIfRateInterval=dellNetIfRateInterval, dellNetIfOutCentRate=dellNetIfOutCentRate, dellNetIfInThrottles=dellNetIfInThrottles, dellNetIfInCentRate=dellNetIfInCentRate, dellNetIfOutOver1023BytePkts=dellNetIfOutOver1023BytePkts, dellNetIfLastDiscontinuityTime=dellNetIfLastDiscontinuityTime, dellNetIfDescr=dellNetIfDescr, dellNetIfAdminStatus=dellNetIfAdminStatus, dellNetifIn65To127BytePkts=dellNetifIn65To127BytePkts, dellNetIfInGiants=dellNetIfInGiants, dellNetIfExtensionMibCompliances=dellNetIfExtensionMibCompliances, dellNetIfEntry=dellNetIfEntry, dellNetIfTxFlowCtrl=dellNetIfTxFlowCtrl, dellNetIfOutWredDrops=dellNetIfOutWredDrops, dellNetIfInVlanPkts=dellNetIfInVlanPkts, dellNetIfOut65To127BytePkts=dellNetIfOut65To127BytePkts, dellNetIfExtensionMibGroups=dellNetIfExtensionMibGroups, dellNetIfOut128To255BytePkts=dellNetIfOut128To255BytePkts, dellNetIfIn512To1023BytePkts=dellNetIfIn512To1023BytePkts, dellNetIfExtensionMibCompliance=dellNetIfExtensionMibCompliance, dellNetIfIn64BytePkts=dellNetIfIn64BytePkts, dellNetIfOutCollisions=dellNetIfOutCollisions, dellNetIfRxFlowCtrl=dellNetIfRxFlowCtrl, dellNetIfOutVlanPkts=dellNetIfOutVlanPkts, dellNetIfParamsGroup=dellNetIfParamsGroup, dellNetIfIn128To255BytePkts=dellNetIfIn128To255BytePkts, dellNetIfStaticsTable=dellNetIfStaticsTable, dellNetIfOutUnderruns=dellNetIfOutUnderruns, dellNetIfIn256To511BytePkts=dellNetIfIn256To511BytePkts, dellNetIfInOverruns=dellNetIfInOverruns, dellNetIfSpeed=dellNetIfSpeed, dellNetIfInOver1023BytePkts=dellNetIfInOver1023BytePkts, dellNetIfStatsGroup=dellNetIfStatsGroup, PYSNMP_MODULE_ID=dellNetIfExtensionMib, dellNetIfExtensionMibObject=dellNetIfExtensionMibObject, dellNetIfExtensionMib=dellNetIfExtensionMib, dellNetIfInRunts=dellNetIfInRunts, dellNetIfOutThrottles=dellNetIfOutThrottles, dellNetIfExtensionParams=dellNetIfExtensionParams, dellNetIfDuplexMode=dellNetIfDuplexMode, dellNetIfPortListBitPos=dellNetIfPortListBitPos, dellNetIfExtensionStats=dellNetIfExtensionStats, dellNetIfOut512To1023BytePkts=dellNetIfOut512To1023BytePkts, dellNetIfQueueingStrategy=dellNetIfQueueingStrategy, dellNetIfOut64BytePkts=dellNetIfOut64BytePkts, dellNetIfStaticsEntry=dellNetIfStaticsEntry, dellNetIfOut256To511BytePkts=dellNetIfOut256To511BytePkts, dellNetIfTable=dellNetIfTable, dellNetIfIpMtu=dellNetIfIpMtu, dellNetIfOutUnicasts=dellNetIfOutUnicasts)