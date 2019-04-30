#
# PySNMP MIB module AT-ATMF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-ATMF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Integer32, Gauge32, Unsigned32, ModuleIdentity, Counter32, IpAddress, TimeTicks, MibIdentifier, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmf = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603))
atmf.setRevisions(('2013-07-15 12:00', '2013-05-27 12:00',))
if mibBuilder.loadTexts: atmf.setLastUpdated('201307151200Z')
if mibBuilder.loadTexts: atmf.setOrganization('Allied Telesis, Inc')
atAtmfTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0))
atAtmfBackupStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 1)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"), ("AT-ATMF-MIB", "atAtmfTrapBackupStatus"))
if mibBuilder.loadTexts: atAtmfBackupStatusTrap.setStatus('current')
atAtmfNodeStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 2)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapNodeStatusChange"), ("AT-ATMF-MIB", "atAtmfTrapNetworkName"))
if mibBuilder.loadTexts: atAtmfNodeStatusChangeTrap.setStatus('current')
atAtmfNodeRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 3)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"), ("AT-ATMF-MIB", "atAtmfTrapNodeRecoveryStatus"))
if mibBuilder.loadTexts: atAtmfNodeRecoveryTrap.setStatus('current')
atAtmfInterfaceStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 4)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapInterfaceName"), ("AT-ATMF-MIB", "atAtmfTrapInterfaceStatusChange"))
if mibBuilder.loadTexts: atAtmfInterfaceStatusChangeTrap.setStatus('current')
atAtmfExternalMediaLowMemoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 5)).setObjects(("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"), ("AT-ATMF-MIB", "atAtmfTrapMediaType"), ("AT-ATMF-MIB", "atAtmfTrapMediaTotal"), ("AT-ATMF-MIB", "atAtmfTrapMediaFree"))
if mibBuilder.loadTexts: atAtmfExternalMediaLowMemoryTrap.setStatus('current')
atAtmfRollingRebootCompleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 6)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"))
if mibBuilder.loadTexts: atAtmfRollingRebootCompleteTrap.setStatus('current')
atAtmfRollingRebootReleaseCompleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 7)).setObjects(("AT-ATMF-MIB", "atAtmfTrapNodeName"), ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"), ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseName"), ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseStatus"))
if mibBuilder.loadTexts: atAtmfRollingRebootReleaseCompleteTrap.setStatus('current')
atAtmfTrapVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1))
atAtmfTrapNodeName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapNodeName.setStatus('current')
atAtmfTrapMasterNodeName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapMasterNodeName.setStatus('current')
atAtmfTrapNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapNetworkName.setStatus('current')
atAtmfTrapInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 4), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapInterfaceName.setStatus('current')
atAtmfTrapBackupStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapBackupStatus.setStatus('current')
atAtmfTrapNodeStatusChange = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("left", 1), ("joined", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapNodeStatusChange.setStatus('current')
atAtmfTrapInterfaceStatusChange = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocking", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapInterfaceStatusChange.setStatus('current')
atAtmfTrapNodeRecoveryStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapNodeRecoveryStatus.setStatus('current')
atAtmfTrapMediaType = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 9), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapMediaType.setStatus('current')
atAtmfTrapMediaTotal = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapMediaTotal.setStatus('current')
atAtmfTrapMediaFree = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapMediaFree.setStatus('current')
atAtmfTrapRollingRebootStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapRollingRebootStatus.setStatus('current')
atAtmfTrapRollingRebootReleaseName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 13), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapRollingRebootReleaseName.setStatus('current')
atAtmfTrapRollingRebootReleaseStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfTrapRollingRebootReleaseStatus.setStatus('current')
atAtmfSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2))
atAtmfSummaryNodeName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryNodeName.setStatus('current')
atAtmfSummaryStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryStatus.setStatus('current')
atAtmfSummaryRole = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("member", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryRole.setStatus('current')
atAtmfSummaryNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 4), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryNetworkName.setStatus('current')
atAtmfSummaryParentName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 5), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryParentName.setStatus('current')
atAtmfSummaryCoreDistance = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryCoreDistance.setStatus('current')
atAtmfSummaryDomainId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryDomainId.setStatus('current')
atAtmfSummaryRestrictedLogin = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryRestrictedLogin.setStatus('current')
atAtmfSummaryNodes = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfSummaryNodes.setStatus('current')
atAtmfNodeTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3), )
if mibBuilder.loadTexts: atAtmfNodeTable.setStatus('current')
atAtmfNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1), ).setIndexNames((0, "AT-ATMF-MIB", "atAtmfNodeName"))
if mibBuilder.loadTexts: atAtmfNodeEntry.setStatus('current')
atAtmfNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAtmfNodeName.setStatus('current')
mibBuilder.exportSymbols("AT-ATMF-MIB", atAtmfTrapRollingRebootReleaseName=atAtmfTrapRollingRebootReleaseName, atAtmfSummaryRole=atAtmfSummaryRole, atAtmfSummaryCoreDistance=atAtmfSummaryCoreDistance, atAtmfSummary=atAtmfSummary, atAtmfTrapInterfaceName=atAtmfTrapInterfaceName, atAtmfTrapNodeRecoveryStatus=atAtmfTrapNodeRecoveryStatus, atAtmfTrapVariable=atAtmfTrapVariable, atAtmfBackupStatusTrap=atAtmfBackupStatusTrap, atAtmfRollingRebootReleaseCompleteTrap=atAtmfRollingRebootReleaseCompleteTrap, atAtmfNodeRecoveryTrap=atAtmfNodeRecoveryTrap, atAtmfSummaryNetworkName=atAtmfSummaryNetworkName, atAtmfInterfaceStatusChangeTrap=atAtmfInterfaceStatusChangeTrap, atAtmfTrapMediaTotal=atAtmfTrapMediaTotal, atAtmfTrapNodeName=atAtmfTrapNodeName, atAtmfTrapMediaFree=atAtmfTrapMediaFree, atAtmfSummaryNodeName=atAtmfSummaryNodeName, atAtmfSummaryRestrictedLogin=atAtmfSummaryRestrictedLogin, atmf=atmf, atAtmfTrapRollingRebootStatus=atAtmfTrapRollingRebootStatus, atAtmfSummaryDomainId=atAtmfSummaryDomainId, atAtmfSummaryNodes=atAtmfSummaryNodes, atAtmfTrapInterfaceStatusChange=atAtmfTrapInterfaceStatusChange, atAtmfRollingRebootCompleteTrap=atAtmfRollingRebootCompleteTrap, atAtmfExternalMediaLowMemoryTrap=atAtmfExternalMediaLowMemoryTrap, atAtmfTrapMediaType=atAtmfTrapMediaType, atAtmfTrapNetworkName=atAtmfTrapNetworkName, PYSNMP_MODULE_ID=atmf, atAtmfTrapMasterNodeName=atAtmfTrapMasterNodeName, atAtmfSummaryStatus=atAtmfSummaryStatus, atAtmfTraps=atAtmfTraps, atAtmfNodeTable=atAtmfNodeTable, atAtmfNodeEntry=atAtmfNodeEntry, atAtmfNodeName=atAtmfNodeName, atAtmfTrapBackupStatus=atAtmfTrapBackupStatus, atAtmfTrapRollingRebootReleaseStatus=atAtmfTrapRollingRebootReleaseStatus, atAtmfSummaryParentName=atAtmfSummaryParentName, atAtmfNodeStatusChangeTrap=atAtmfNodeStatusChangeTrap, atAtmfTrapNodeStatusChange=atAtmfTrapNodeStatusChange)