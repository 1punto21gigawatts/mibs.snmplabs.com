#
# PySNMP MIB module CISCO-NBAR-PROTOCOL-DISCOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NBAR-PROTOCOL-DISCOVERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Bits, iso, MibIdentifier, Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "MibIdentifier", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
ciscoNbarProtocolDiscoveryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 244))
ciscoNbarProtocolDiscoveryMIB.setRevisions(('2002-08-16 00:00', '2001-12-28 00:00',))
if mibBuilder.loadTexts: ciscoNbarProtocolDiscoveryMIB.setLastUpdated('200208160000Z')
if mibBuilder.loadTexts: ciscoNbarProtocolDiscoveryMIB.setOrganization('Cisco Systems, Inc.')
class CiscoPdProtocolIndex(TextualConvention, Unsigned32):
    status = 'current'

class CiscoPdProtocolName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CiscoPdDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("bitRateIn", 1), ("bitRateOut", 2), ("bitRateSum", 3), ("byteCountIn", 4), ("byteCountOut", 5), ("byteCountSum", 6), ("packetCountIn", 7), ("packetCountOut", 8), ("packetCountSum", 9))

cnpdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 0))
cnpdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1))
cnpdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 2))
cnpdStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1))
cnpdAllStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2))
cnpdTopNConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3))
cnpdTopNStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4))
cnpdThresholdConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5))
cnpdThresholdHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6))
cnpdNotificationsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 7))
cnpdSupportedProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8))
cnpdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 1))
cnpdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2))
cnpdSupportedProtocolsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1), )
if mibBuilder.loadTexts: cnpdSupportedProtocolsTable.setStatus('current')
cnpdSupportedProtocolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1), ).setIndexNames((0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdSupportedProtocolsIndex"))
if mibBuilder.loadTexts: cnpdSupportedProtocolsEntry.setStatus('current')
cnpdSupportedProtocolsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1, 1), CiscoPdProtocolIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: cnpdSupportedProtocolsIndex.setStatus('current')
cnpdSupportedProtocolsName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 8, 1, 1, 2), CiscoPdProtocolName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdSupportedProtocolsName.setStatus('current')
cnpdStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1), )
if mibBuilder.loadTexts: cnpdStatusTable.setStatus('current')
cnpdStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cnpdStatusEntry.setStatus('current')
cnpdStatusPdEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnpdStatusPdEnable.setStatus('current')
cnpdStatusLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdStatusLastUpdateTime.setStatus('current')
cnpdAllStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1), )
if mibBuilder.loadTexts: cnpdAllStatsTable.setStatus('current')
cnpdAllStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsProtocolsIndex"))
if mibBuilder.loadTexts: cnpdAllStatsEntry.setStatus('current')
cnpdAllStatsProtocolsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 1), CiscoPdProtocolIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: cnpdAllStatsProtocolsIndex.setStatus('current')
cnpdAllStatsProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 2), CiscoPdProtocolName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsProtocolName.setStatus('current')
cnpdAllStatsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsInPkts.setStatus('current')
cnpdAllStatsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsOutPkts.setStatus('current')
cnpdAllStatsInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsInBytes.setStatus('current')
cnpdAllStatsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 6), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsOutBytes.setStatus('current')
cnpdAllStatsHCInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 7), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsHCInPkts.setStatus('current')
cnpdAllStatsHCOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 8), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsHCOutPkts.setStatus('current')
cnpdAllStatsHCInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 9), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsHCInBytes.setStatus('current')
cnpdAllStatsHCOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 10), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsHCOutBytes.setStatus('current')
cnpdAllStatsInBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('kilo bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsInBitRate.setStatus('current')
cnpdAllStatsOutBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 2, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('kilo bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdAllStatsOutBitRate.setStatus('current')
cnpdTopNConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1), )
if mibBuilder.loadTexts: cnpdTopNConfigTable.setStatus('current')
cnpdTopNConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIndex"))
if mibBuilder.loadTexts: cnpdTopNConfigEntry.setStatus('current')
cnpdTopNConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: cnpdTopNConfigIndex.setStatus('current')
cnpdTopNConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdTopNConfigIfIndex.setStatus('current')
cnpdTopNConfigStatsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 3), CiscoPdDataType().clone('byteCountSum')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdTopNConfigStatsSelect.setStatus('current')
cnpdTopNConfigSampleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdTopNConfigSampleTime.setStatus('current')
cnpdTopNConfigRequestedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 500)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdTopNConfigRequestedSize.setStatus('current')
cnpdTopNConfigGrantedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdTopNConfigGrantedSize.setStatus('current')
cnpdTopNConfigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdTopNConfigTime.setStatus('current')
cnpdTopNConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 3, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdTopNConfigStatus.setStatus('current')
cnpdTopNStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1), )
if mibBuilder.loadTexts: cnpdTopNStatsTable.setStatus('current')
cnpdTopNStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIndex"), (0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsIndex"))
if mibBuilder.loadTexts: cnpdTopNStatsEntry.setStatus('current')
cnpdTopNStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 500)))
if mibBuilder.loadTexts: cnpdTopNStatsIndex.setStatus('current')
cnpdTopNStatsProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 2), CiscoPdProtocolName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdTopNStatsProtocolName.setStatus('current')
cnpdTopNStatsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdTopNStatsRate.setStatus('current')
cnpdTopNStatsHCRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 4, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdTopNStatsHCRate.setStatus('current')
cnpdThresholdConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1), )
if mibBuilder.loadTexts: cnpdThresholdConfigTable.setStatus('current')
cnpdThresholdConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIndex"))
if mibBuilder.loadTexts: cnpdThresholdConfigEntry.setStatus('current')
cnpdThresholdConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: cnpdThresholdConfigIndex.setStatus('current')
cnpdThresholdConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigIfIndex.setStatus('current')
cnpdThresholdConfigInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigInterval.setStatus('current')
cnpdThresholdConfigSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2))).clone('absoluteValue')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigSampleType.setStatus('current')
cnpdThresholdConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 5), CiscoPdProtocolIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigProtocol.setStatus('current')
cnpdThresholdConfigProtocolAny = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigProtocolAny.setStatus('current')
cnpdThresholdConfigStatsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 7), CiscoPdDataType().clone('bitRateSum')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigStatsSelect.setStatus('current')
cnpdThresholdConfigStartup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2), ("risingOrFalling", 3))).clone('risingOrFalling')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigStartup.setStatus('current')
cnpdThresholdConfigRising = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigRising.setStatus('current')
cnpdThresholdConfigFalling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigFalling.setStatus('current')
cnpdThresholdConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 5, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnpdThresholdConfigStatus.setStatus('current')
cnpdThresholdHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1), )
if mibBuilder.loadTexts: cnpdThresholdHistoryTable.setStatus('current')
cnpdThresholdHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryIndex"))
if mibBuilder.loadTexts: cnpdThresholdHistoryEntry.setStatus('current')
cnpdThresholdHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: cnpdThresholdHistoryIndex.setStatus('current')
cnpdThresholdHistoryConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryConfigIndex.setStatus('current')
cnpdThresholdHistoryValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryValue.setStatus('current')
cnpdThresholdHistoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("risingBreach", 1), ("fallingBreach", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryType.setStatus('current')
cnpdThresholdHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryTime.setStatus('current')
cnpdThresholdHistoryProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 6), CiscoPdProtocolIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryProtocol.setStatus('current')
cnpdThresholdHistoryStatsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 6, 1, 1, 7), CiscoPdDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnpdThresholdHistoryStatsSelect.setStatus('current')
cnpdNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 244, 1, 7, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnpdNotificationsEnable.setStatus('current')
cnpdThresholdRisingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 244, 0, 1)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigRising"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"))
if mibBuilder.loadTexts: cnpdThresholdRisingEvent.setStatus('current')
cnpdThresholdFallingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 244, 0, 2)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigFalling"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"))
if mibBuilder.loadTexts: cnpdThresholdFallingEvent.setStatus('current')
cnpdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 1, 1)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdStatsGroup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNGroup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdGroup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdMIBNotificationsGroup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdMIBNotificationsConfigGroup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdSupportedProtocolsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdMIBCompliance = cnpdMIBCompliance.setStatus('current')
cnpdStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 1)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdStatusPdEnable"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdStatusLastUpdateTime"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsProtocolName"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInPkts"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutPkts"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInBytes"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutBytes"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCInPkts"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCOutPkts"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCInBytes"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsHCOutBytes"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsInBitRate"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdAllStatsOutBitRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdStatsGroup = cnpdStatsGroup.setStatus('current')
cnpdTopNGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 2)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigIfIndex"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigStatsSelect"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigRequestedSize"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigSampleTime"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigGrantedSize"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigTime"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNConfigStatus"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsProtocolName"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsRate"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdTopNStatsHCRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdTopNGroup = cnpdTopNGroup.setStatus('current')
cnpdThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 3)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigIfIndex"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigInterval"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigSampleType"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocol"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatsSelect"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigProtocolAny"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStartup"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigRising"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigFalling"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdConfigStatus"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryConfigIndex"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryValue"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryType"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryTime"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryProtocol"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdHistoryStatsSelect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdThresholdGroup = cnpdThresholdGroup.setStatus('current')
cnpdMIBNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 4)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdRisingEvent"), ("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdThresholdFallingEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdMIBNotificationsGroup = cnpdMIBNotificationsGroup.setStatus('current')
cnpdMIBNotificationsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 5)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdNotificationsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdMIBNotificationsConfigGroup = cnpdMIBNotificationsConfigGroup.setStatus('current')
cnpdSupportedProtocolsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 244, 2, 2, 6)).setObjects(("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", "cnpdSupportedProtocolsName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnpdSupportedProtocolsGroup = cnpdSupportedProtocolsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NBAR-PROTOCOL-DISCOVERY-MIB", cnpdTopNConfigIndex=cnpdTopNConfigIndex, cnpdThresholdConfigInterval=cnpdThresholdConfigInterval, cnpdTopNConfigEntry=cnpdTopNConfigEntry, CiscoPdDataType=CiscoPdDataType, cnpdThresholdConfig=cnpdThresholdConfig, cnpdTopNStatsProtocolName=cnpdTopNStatsProtocolName, cnpdSupportedProtocols=cnpdSupportedProtocols, cnpdThresholdHistoryIndex=cnpdThresholdHistoryIndex, cnpdMIBGroups=cnpdMIBGroups, CiscoPdProtocolIndex=CiscoPdProtocolIndex, cnpdStatusEntry=cnpdStatusEntry, CiscoPdProtocolName=CiscoPdProtocolName, cnpdMIBNotificationsConfigGroup=cnpdMIBNotificationsConfigGroup, cnpdAllStatsInBitRate=cnpdAllStatsInBitRate, cnpdThresholdHistory=cnpdThresholdHistory, cnpdThresholdFallingEvent=cnpdThresholdFallingEvent, cnpdSupportedProtocolsEntry=cnpdSupportedProtocolsEntry, cnpdStatusPdEnable=cnpdStatusPdEnable, cnpdTopNConfigGrantedSize=cnpdTopNConfigGrantedSize, cnpdNotificationsConfig=cnpdNotificationsConfig, cnpdMIBObjects=cnpdMIBObjects, cnpdStatusLastUpdateTime=cnpdStatusLastUpdateTime, cnpdThresholdConfigFalling=cnpdThresholdConfigFalling, cnpdTopNConfigTime=cnpdTopNConfigTime, cnpdThresholdConfigProtocol=cnpdThresholdConfigProtocol, cnpdStatus=cnpdStatus, cnpdNotificationsEnable=cnpdNotificationsEnable, cnpdTopNConfig=cnpdTopNConfig, cnpdAllStatsOutBytes=cnpdAllStatsOutBytes, cnpdTopNConfigStatsSelect=cnpdTopNConfigStatsSelect, cnpdAllStatsEntry=cnpdAllStatsEntry, cnpdMIBCompliances=cnpdMIBCompliances, cnpdThresholdHistoryStatsSelect=cnpdThresholdHistoryStatsSelect, cnpdTopNStatsIndex=cnpdTopNStatsIndex, PYSNMP_MODULE_ID=ciscoNbarProtocolDiscoveryMIB, cnpdTopNStatsTable=cnpdTopNStatsTable, cnpdThresholdConfigIfIndex=cnpdThresholdConfigIfIndex, cnpdTopNConfigRequestedSize=cnpdTopNConfigRequestedSize, cnpdTopNStatsEntry=cnpdTopNStatsEntry, cnpdTopNConfigStatus=cnpdTopNConfigStatus, cnpdTopNStatsRate=cnpdTopNStatsRate, cnpdAllStatsHCInBytes=cnpdAllStatsHCInBytes, cnpdAllStatsTable=cnpdAllStatsTable, cnpdTopNStatsHCRate=cnpdTopNStatsHCRate, cnpdThresholdHistoryConfigIndex=cnpdThresholdHistoryConfigIndex, cnpdThresholdHistoryProtocol=cnpdThresholdHistoryProtocol, cnpdThresholdConfigTable=cnpdThresholdConfigTable, cnpdThresholdHistoryTime=cnpdThresholdHistoryTime, cnpdTopNConfigSampleTime=cnpdTopNConfigSampleTime, cnpdTopNConfigIfIndex=cnpdTopNConfigIfIndex, cnpdSupportedProtocolsName=cnpdSupportedProtocolsName, cnpdSupportedProtocolsIndex=cnpdSupportedProtocolsIndex, cnpdThresholdConfigStatsSelect=cnpdThresholdConfigStatsSelect, cnpdAllStatsHCInPkts=cnpdAllStatsHCInPkts, cnpdThresholdConfigStatus=cnpdThresholdConfigStatus, cnpdAllStatsProtocolsIndex=cnpdAllStatsProtocolsIndex, cnpdThresholdConfigIndex=cnpdThresholdConfigIndex, cnpdThresholdConfigSampleType=cnpdThresholdConfigSampleType, cnpdThresholdHistoryTable=cnpdThresholdHistoryTable, cnpdAllStatsInBytes=cnpdAllStatsInBytes, cnpdMIBConformance=cnpdMIBConformance, cnpdMIBNotifications=cnpdMIBNotifications, cnpdTopNStats=cnpdTopNStats, cnpdThresholdConfigEntry=cnpdThresholdConfigEntry, cnpdAllStatsInPkts=cnpdAllStatsInPkts, cnpdThresholdConfigStartup=cnpdThresholdConfigStartup, cnpdAllStatsOutPkts=cnpdAllStatsOutPkts, ciscoNbarProtocolDiscoveryMIB=ciscoNbarProtocolDiscoveryMIB, cnpdThresholdConfigRising=cnpdThresholdConfigRising, cnpdAllStats=cnpdAllStats, cnpdStatusTable=cnpdStatusTable, cnpdThresholdHistoryValue=cnpdThresholdHistoryValue, cnpdThresholdGroup=cnpdThresholdGroup, cnpdThresholdHistoryType=cnpdThresholdHistoryType, cnpdTopNConfigTable=cnpdTopNConfigTable, cnpdThresholdRisingEvent=cnpdThresholdRisingEvent, cnpdAllStatsHCOutBytes=cnpdAllStatsHCOutBytes, cnpdTopNGroup=cnpdTopNGroup, cnpdAllStatsProtocolName=cnpdAllStatsProtocolName, cnpdThresholdConfigProtocolAny=cnpdThresholdConfigProtocolAny, cnpdSupportedProtocolsTable=cnpdSupportedProtocolsTable, cnpdMIBCompliance=cnpdMIBCompliance, cnpdStatsGroup=cnpdStatsGroup, cnpdThresholdHistoryEntry=cnpdThresholdHistoryEntry, cnpdSupportedProtocolsGroup=cnpdSupportedProtocolsGroup, cnpdAllStatsOutBitRate=cnpdAllStatsOutBitRate, cnpdMIBNotificationsGroup=cnpdMIBNotificationsGroup, cnpdAllStatsHCOutPkts=cnpdAllStatsHCOutPkts)