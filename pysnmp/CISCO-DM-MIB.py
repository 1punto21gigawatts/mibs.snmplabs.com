#
# PySNMP MIB module CISCO-DM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
cffFcFeElementName, = mibBuilder.importSymbols("CISCO-FC-FE-MIB", "cffFcFeElementName")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, FcNameId, FcNameIdOrZero, DomainId, DomainIdOrZero = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId", "FcNameId", "FcNameIdOrZero", "DomainId", "DomainIdOrZero")
notifyVsanIndex, vsanIndex = mibBuilder.importSymbols("CISCO-VSAN-MIB", "notifyVsanIndex", "vsanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, IpAddress, Counter32, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "MibIdentifier", "iso", "Bits")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
ciscoDmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 302))
ciscoDmMIB.setRevisions(('2003-09-22 00:00', '2003-06-20 00:00', '2003-02-27 00:00', '2003-02-21 00:00', '2003-01-28 00:00', '2003-01-02 00:00', '2002-10-04 00:00',))
if mibBuilder.loadTexts: ciscoDmMIB.setLastUpdated('200309220000Z')
if mibBuilder.loadTexts: ciscoDmMIB.setOrganization('Cisco Systems Inc. ')
ciscoDmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 1))
dmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 2))
dmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1))
dmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2))
dmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3))
class DomainPriority(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class DomainPriorityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class DomainInterfaceRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("nonPrincipal", 1), ("principalUpstream", 2), ("principalDownsteam", 3), ("isolated", 4), ("down", 5), ("unknown", 6))

class DmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("starting", 1), ("unconfigured", 2), ("principalSwitchSelection", 3), ("domainIdDistribution", 4), ("buildFabricPhase", 5), ("reconfigureFabricPhase", 6), ("stable", 7), ("stableWithNoEports", 8), ("stableWithDomainConfigured", 9), ("noDomains", 10), ("disabled", 11), ("suspended", 12), ("unknown", 13))

dmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1), )
if mibBuilder.loadTexts: dmTable.setStatus('current')
dmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: dmEntry.setStatus('current')
dmConfigDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 1), DomainIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmConfigDomainId.setStatus('current')
dmConfigDomainIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("preferred", 2))).clone('preferred')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmConfigDomainIdType.setStatus('current')
dmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmEnable.setStatus('current')
dmAutoReconfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmAutoReconfigure.setStatus('current')
dmContiguousAllocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmContiguousAllocation.setStatus('current')
dmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 6), DomainPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmPriority.setStatus('current')
dmRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonDisruptive", 1), ("disruptive", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmRestart.setStatus('current')
dmFabricName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 8), FcNameIdOrZero().clone(hexValue="20010005300028df")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmFabricName.setStatus('current')
dmPrincipalSwitchWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 9), FcNameIdOrZero().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmPrincipalSwitchWwn.setStatus('current')
dmLocalSwitchWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 10), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmLocalSwitchWwn.setStatus('current')
dmAssignedAreaIdList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmAssignedAreaIdList.setStatus('current')
dmFcIdsGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFcIdsGranted.setStatus('current')
dmFcIdsRecovered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFcIdsRecovered.setStatus('current')
dmFreeFcIds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFreeFcIds.setStatus('current')
dmAssignedFcIds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmAssignedFcIds.setStatus('current')
dmReservedFcIds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmReservedFcIds.setStatus('current')
dmRunningPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 17), DomainPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmRunningPriority.setStatus('current')
dmPrincSwRunningPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 18), DomainPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmPrincSwRunningPriority.setStatus('current')
dmState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 19), DmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmState.setStatus('current')
dmPrincipalSwitchSelections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmPrincipalSwitchSelections.setStatus('current')
dmBuildFabrics = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmBuildFabrics.setStatus('current')
dmFabricReconfigures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFabricReconfigures.setStatus('current')
dmDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 23), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmDomainId.setStatus('current')
dmLocalPrincipalSwitchSelctns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmLocalPrincipalSwitchSelctns.setStatus('current')
dmFcIdPersistency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 25), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmFcIdPersistency.setStatus('current')
dmFcIdPurge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmFcIdPurge.setStatus('current')
dmIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2), )
if mibBuilder.loadTexts: dmIfTable.setStatus('current')
dmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dmIfEntry.setStatus('current')
dmIfRcfReject = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmIfRcfReject.setStatus('current')
dmIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 2), DomainInterfaceRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmIfRole.setStatus('current')
dmIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmIfRowStatus.setStatus('current')
dmAreaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1), )
if mibBuilder.loadTexts: dmAreaTable.setStatus('current')
dmAreaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-DM-MIB", "dmAreaAreaId"))
if mibBuilder.loadTexts: dmAreaEntry.setStatus('current')
dmAreaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: dmAreaAreaId.setStatus('current')
dmAreaAssignedPortIdList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmAreaAssignedPortIdList.setStatus('current')
dmDatabaseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2), )
if mibBuilder.loadTexts: dmDatabaseTable.setStatus('current')
dmDatabaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-DM-MIB", "dmDatabaseDomainId"))
if mibBuilder.loadTexts: dmDatabaseEntry.setStatus('current')
dmDatabaseDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1, 1), DomainId())
if mibBuilder.loadTexts: dmDatabaseDomainId.setStatus('current')
dmDatabaseSwitchWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1, 2), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmDatabaseSwitchWwn.setStatus('current')
dmMaxFcIdCacheSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmMaxFcIdCacheSize.setStatus('current')
dmFcIdCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4), )
if mibBuilder.loadTexts: dmFcIdCacheTable.setStatus('current')
dmFcIdCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-DM-MIB", "dmFcIdCacheWwn"))
if mibBuilder.loadTexts: dmFcIdCacheEntry.setStatus('current')
dmFcIdCacheWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 1), FcNameId())
if mibBuilder.loadTexts: dmFcIdCacheWwn.setStatus('current')
dmFcIdCacheAreaIdPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFcIdCacheAreaIdPortId.setStatus('current')
dmFcIdCachePortIds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFcIdCachePortIds.setStatus('current')
dmReConfFabricChangeNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmReConfFabricChangeNotifyEnable.setStatus('current')
dmFcIdPersistencyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4), )
if mibBuilder.loadTexts: dmFcIdPersistencyTable.setStatus('current')
dmFcIdPersistencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-DM-MIB", "dmFcIdPersistencyWwn"))
if mibBuilder.loadTexts: dmFcIdPersistencyEntry.setStatus('current')
dmFcIdPersistencyWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 1), FcNameId())
if mibBuilder.loadTexts: dmFcIdPersistencyWwn.setStatus('current')
dmFcIdPersistencyFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 2), FcAddressId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmFcIdPersistencyFcId.setStatus('current')
dmFcIdPersistencyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one", 1), ("area", 2))).clone('one')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmFcIdPersistencyNum.setStatus('current')
dmFcIdPersistencyUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmFcIdPersistencyUsed.setStatus('current')
dmFcIdPersistencyType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2))).clone('static')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmFcIdPersistencyType.setStatus('current')
dmFcIdPersistencyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dmFcIdPersistencyRowStatus.setStatus('current')
dmAllowedDomainIDListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5), )
if mibBuilder.loadTexts: dmAllowedDomainIDListTable.setStatus('current')
dmAllowedDomainIDListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-DM-MIB", "dmAllowedDomainIDListId"))
if mibBuilder.loadTexts: dmAllowedDomainIDListEntry.setStatus('current')
dmAllowedDomainIDListId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: dmAllowedDomainIDListId.setStatus('current')
dmAllowedDomainIDList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmAllowedDomainIDList.setStatus('current')
dmAllowedDomainIDListUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmAllowedDomainIDListUser.setStatus('current')
dmNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0))
dmDomainIdNotAssignedNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 1)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-FC-FE-MIB", "cffFcFeElementName"))
if mibBuilder.loadTexts: dmDomainIdNotAssignedNotify.setStatus('current')
dmNewPrincipalSwitchNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 2)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-FC-FE-MIB", "cffFcFeElementName"))
if mibBuilder.loadTexts: dmNewPrincipalSwitchNotify.setStatus('current')
dmFabricChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 3)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"))
if mibBuilder.loadTexts: dmFabricChangeNotify.setStatus('current')
dmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1))
dmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2))
dmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 1)).setObjects(("CISCO-DM-MIB", "dmGroup"), ("CISCO-DM-MIB", "dmDatabaseGroup"), ("CISCO-DM-MIB", "dmAreaGroup"), ("CISCO-DM-MIB", "dmCacheGroup"), ("CISCO-DM-MIB", "dmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmMIBCompliance = dmMIBCompliance.setStatus('deprecated')
dmMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 2)).setObjects(("CISCO-DM-MIB", "dmGroupRev1"), ("CISCO-DM-MIB", "dmDatabaseGroup"), ("CISCO-DM-MIB", "dmAreaGroup"), ("CISCO-DM-MIB", "dmCacheGroup"), ("CISCO-DM-MIB", "dmNotificationGroup"), ("CISCO-DM-MIB", "dmFcIdPersistencyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmMIBCompliance1 = dmMIBCompliance1.setStatus('deprecated')
dmMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 3)).setObjects(("CISCO-DM-MIB", "dmGroupRev1"), ("CISCO-DM-MIB", "dmDatabaseGroup"), ("CISCO-DM-MIB", "dmAreaGroup"), ("CISCO-DM-MIB", "dmCacheGroup"), ("CISCO-DM-MIB", "dmNotificationGroup"), ("CISCO-DM-MIB", "dmFcIdPersistencyGroup"), ("CISCO-DM-MIB", "dmDomainIDAllowedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmMIBCompliance2 = dmMIBCompliance2.setStatus('current')
dmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 1)).setObjects(("CISCO-DM-MIB", "dmConfigDomainId"), ("CISCO-DM-MIB", "dmConfigDomainIdType"), ("CISCO-DM-MIB", "dmEnable"), ("CISCO-DM-MIB", "dmAutoReconfigure"), ("CISCO-DM-MIB", "dmContiguousAllocation"), ("CISCO-DM-MIB", "dmPriority"), ("CISCO-DM-MIB", "dmRestart"), ("CISCO-DM-MIB", "dmFabricName"), ("CISCO-DM-MIB", "dmPrincipalSwitchWwn"), ("CISCO-DM-MIB", "dmLocalSwitchWwn"), ("CISCO-DM-MIB", "dmAssignedAreaIdList"), ("CISCO-DM-MIB", "dmFcIdsGranted"), ("CISCO-DM-MIB", "dmFcIdsRecovered"), ("CISCO-DM-MIB", "dmFreeFcIds"), ("CISCO-DM-MIB", "dmAssignedFcIds"), ("CISCO-DM-MIB", "dmReservedFcIds"), ("CISCO-DM-MIB", "dmRunningPriority"), ("CISCO-DM-MIB", "dmPrincSwRunningPriority"), ("CISCO-DM-MIB", "dmState"), ("CISCO-DM-MIB", "dmPrincipalSwitchSelections"), ("CISCO-DM-MIB", "dmBuildFabrics"), ("CISCO-DM-MIB", "dmFabricReconfigures"), ("CISCO-DM-MIB", "dmDomainId"), ("CISCO-DM-MIB", "dmReConfFabricChangeNotifyEnable"), ("CISCO-DM-MIB", "dmIfRcfReject"), ("CISCO-DM-MIB", "dmIfRole"), ("CISCO-DM-MIB", "dmIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmGroup = dmGroup.setStatus('deprecated')
dmDatabaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 2)).setObjects(("CISCO-DM-MIB", "dmDatabaseSwitchWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmDatabaseGroup = dmDatabaseGroup.setStatus('current')
dmAreaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 3)).setObjects(("CISCO-DM-MIB", "dmAreaAssignedPortIdList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmAreaGroup = dmAreaGroup.setStatus('current')
dmCacheGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 4)).setObjects(("CISCO-DM-MIB", "dmMaxFcIdCacheSize"), ("CISCO-DM-MIB", "dmFcIdCacheAreaIdPortId"), ("CISCO-DM-MIB", "dmFcIdCachePortIds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmCacheGroup = dmCacheGroup.setStatus('current')
dmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 5)).setObjects(("CISCO-DM-MIB", "dmDomainIdNotAssignedNotify"), ("CISCO-DM-MIB", "dmNewPrincipalSwitchNotify"), ("CISCO-DM-MIB", "dmFabricChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmNotificationGroup = dmNotificationGroup.setStatus('current')
dmGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 6)).setObjects(("CISCO-DM-MIB", "dmConfigDomainId"), ("CISCO-DM-MIB", "dmConfigDomainIdType"), ("CISCO-DM-MIB", "dmEnable"), ("CISCO-DM-MIB", "dmAutoReconfigure"), ("CISCO-DM-MIB", "dmContiguousAllocation"), ("CISCO-DM-MIB", "dmPriority"), ("CISCO-DM-MIB", "dmRestart"), ("CISCO-DM-MIB", "dmFabricName"), ("CISCO-DM-MIB", "dmPrincipalSwitchWwn"), ("CISCO-DM-MIB", "dmLocalSwitchWwn"), ("CISCO-DM-MIB", "dmAssignedAreaIdList"), ("CISCO-DM-MIB", "dmFcIdsGranted"), ("CISCO-DM-MIB", "dmFcIdsRecovered"), ("CISCO-DM-MIB", "dmFreeFcIds"), ("CISCO-DM-MIB", "dmAssignedFcIds"), ("CISCO-DM-MIB", "dmReservedFcIds"), ("CISCO-DM-MIB", "dmRunningPriority"), ("CISCO-DM-MIB", "dmPrincSwRunningPriority"), ("CISCO-DM-MIB", "dmState"), ("CISCO-DM-MIB", "dmPrincipalSwitchSelections"), ("CISCO-DM-MIB", "dmBuildFabrics"), ("CISCO-DM-MIB", "dmFabricReconfigures"), ("CISCO-DM-MIB", "dmDomainId"), ("CISCO-DM-MIB", "dmLocalPrincipalSwitchSelctns"), ("CISCO-DM-MIB", "dmReConfFabricChangeNotifyEnable"), ("CISCO-DM-MIB", "dmIfRcfReject"), ("CISCO-DM-MIB", "dmIfRole"), ("CISCO-DM-MIB", "dmIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmGroupRev1 = dmGroupRev1.setStatus('current')
dmFcIdPersistencyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 7)).setObjects(("CISCO-DM-MIB", "dmFcIdPersistency"), ("CISCO-DM-MIB", "dmFcIdPurge"), ("CISCO-DM-MIB", "dmFcIdPersistencyFcId"), ("CISCO-DM-MIB", "dmFcIdPersistencyNum"), ("CISCO-DM-MIB", "dmFcIdPersistencyUsed"), ("CISCO-DM-MIB", "dmFcIdPersistencyType"), ("CISCO-DM-MIB", "dmFcIdPersistencyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmFcIdPersistencyGroup = dmFcIdPersistencyGroup.setStatus('current')
dmDomainIDAllowedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 8)).setObjects(("CISCO-DM-MIB", "dmAllowedDomainIDList"), ("CISCO-DM-MIB", "dmAllowedDomainIDListUser"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmDomainIDAllowedGroup = dmDomainIDAllowedGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DM-MIB", dmPriority=dmPriority, dmMIBCompliance1=dmMIBCompliance1, dmEntry=dmEntry, dmAreaAreaId=dmAreaAreaId, dmConfigDomainId=dmConfigDomainId, dmGroup=dmGroup, dmIfTable=dmIfTable, dmAllowedDomainIDListUser=dmAllowedDomainIDListUser, dmFcIdPersistencyRowStatus=dmFcIdPersistencyRowStatus, PYSNMP_MODULE_ID=ciscoDmMIB, dmNewPrincipalSwitchNotify=dmNewPrincipalSwitchNotify, dmPrincipalSwitchWwn=dmPrincipalSwitchWwn, dmPrincipalSwitchSelections=dmPrincipalSwitchSelections, dmContiguousAllocation=dmContiguousAllocation, ciscoDmMIBObjects=ciscoDmMIBObjects, dmIfEntry=dmIfEntry, dmDomainId=dmDomainId, dmFcIdCacheWwn=dmFcIdCacheWwn, dmIfRowStatus=dmIfRowStatus, ciscoDmMIB=ciscoDmMIB, dmNotificationGroup=dmNotificationGroup, dmMaxFcIdCacheSize=dmMaxFcIdCacheSize, dmFcIdPersistencyUsed=dmFcIdPersistencyUsed, dmFcIdPersistencyEntry=dmFcIdPersistencyEntry, dmAreaTable=dmAreaTable, dmAssignedAreaIdList=dmAssignedAreaIdList, DomainPriority=DomainPriority, dmDomainIdNotAssignedNotify=dmDomainIdNotAssignedNotify, dmFcIdCacheEntry=dmFcIdCacheEntry, dmFcIdsGranted=dmFcIdsGranted, dmMIBConformance=dmMIBConformance, dmFcIdCachePortIds=dmFcIdCachePortIds, dmMIBCompliance2=dmMIBCompliance2, dmLocalPrincipalSwitchSelctns=dmLocalPrincipalSwitchSelctns, dmFcIdPersistencyNum=dmFcIdPersistencyNum, dmFcIdPersistencyFcId=dmFcIdPersistencyFcId, dmFreeFcIds=dmFreeFcIds, dmFcIdPersistency=dmFcIdPersistency, dmFcIdPersistencyWwn=dmFcIdPersistencyWwn, dmDatabaseEntry=dmDatabaseEntry, dmRestart=dmRestart, dmGroupRev1=dmGroupRev1, dmDatabaseTable=dmDatabaseTable, dmAllowedDomainIDListTable=dmAllowedDomainIDListTable, dmAreaAssignedPortIdList=dmAreaAssignedPortIdList, dmFcIdCacheAreaIdPortId=dmFcIdCacheAreaIdPortId, dmFcIdsRecovered=dmFcIdsRecovered, dmFcIdCacheTable=dmFcIdCacheTable, dmRunningPriority=dmRunningPriority, dmAreaGroup=dmAreaGroup, dmNotificationPrefix=dmNotificationPrefix, dmMIBCompliance=dmMIBCompliance, dmDomainIDAllowedGroup=dmDomainIDAllowedGroup, dmMIBGroups=dmMIBGroups, dmAllowedDomainIDListEntry=dmAllowedDomainIDListEntry, dmDatabaseGroup=dmDatabaseGroup, dmInfo=dmInfo, dmDatabaseDomainId=dmDatabaseDomainId, dmAssignedFcIds=dmAssignedFcIds, dmConfiguration=dmConfiguration, dmIfRole=dmIfRole, dmDatabaseSwitchWwn=dmDatabaseSwitchWwn, dmLocalSwitchWwn=dmLocalSwitchWwn, dmAutoReconfigure=dmAutoReconfigure, dmFabricChangeNotify=dmFabricChangeNotify, dmEnable=dmEnable, dmConfigDomainIdType=dmConfigDomainIdType, dmFcIdPersistencyGroup=dmFcIdPersistencyGroup, DomainInterfaceRole=DomainInterfaceRole, dmFcIdPersistencyType=dmFcIdPersistencyType, dmAllowedDomainIDListId=dmAllowedDomainIDListId, dmReConfFabricChangeNotifyEnable=dmReConfFabricChangeNotifyEnable, dmIfRcfReject=dmIfRcfReject, dmAreaEntry=dmAreaEntry, dmBuildFabrics=dmBuildFabrics, dmMIBCompliances=dmMIBCompliances, dmPrincSwRunningPriority=dmPrincSwRunningPriority, dmFcIdPurge=dmFcIdPurge, dmFabricReconfigures=dmFabricReconfigures, dmTable=dmTable, DomainPriorityOrZero=DomainPriorityOrZero, DmState=DmState, dmFcIdPersistencyTable=dmFcIdPersistencyTable, dmState=dmState, dmReservedFcIds=dmReservedFcIds, dmCacheGroup=dmCacheGroup, dmFabricName=dmFabricName, dmAllowedDomainIDList=dmAllowedDomainIDList, dmNotification=dmNotification)