#
# PySNMP MIB module ZYXEL-IGMP-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-IGMP-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, NotificationType, Counter32, Gauge32, MibIdentifier, Integer32, Unsigned32, Bits, IpAddress, Counter64, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "NotificationType", "Counter32", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "Bits", "IpAddress", "Counter64", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIgmpSnooping = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31))
if mibBuilder.loadTexts: zyxelIgmpSnooping.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIgmpSnooping.setOrganization('Enterprise Solution ZyXEL')
zyxelIgmpSnoopingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1))
zyxelIgmpSnoopingStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2))
zyIgmpSnoopingState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingState.setStatus('current')
zyIgmpSnoopingGroupHostTimeout = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupHostTimeout.setStatus('current')
zyIgmpSnooping8021pPriority = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnooping8021pPriority.setStatus('current')
zyIgmpSnoopingVlanMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("fixed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingVlanMode.setStatus('current')
zyIgmpSnoopingMaxNumberOfVlans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingMaxNumberOfVlans.setStatus('current')
zyxelIgmpSnoopingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingVlanTable.setStatus('current')
zyxelIgmpSnoopingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingVlanVid"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingVlanEntry.setStatus('current')
zyIgmpSnoopingVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingVlanVid.setStatus('current')
zyIgmpSnoopingVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingVlanName.setStatus('current')
zyIgmpSnoopingVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyIgmpSnoopingVlanRowStatus.setStatus('current')
zyIgmpSnoopingQuerierModeState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 7), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingQuerierModeState.setStatus('current')
zyIgmpSnoopingReportProxyState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 8), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingReportProxyState.setStatus('current')
zyxelIgmpSnoopingPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingPortTable.setStatus('current')
zyxelIgmpSnoopingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingPortEntry.setStatus('current')
zyIgmpSnoopingPortMaxGroupLimitedState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortMaxGroupLimitedState.setStatus('current')
zyIgmpSnoopingPortMaxOfGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortMaxOfGroups.setStatus('current')
zyIgmpSnoopingPortQuerierMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("fixed", 2), ("edge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortQuerierMode.setStatus('current')
zyIgmpSnoopingPortThrottlingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("replace", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortThrottlingAction.setStatus('current')
zyIgmpSnoopingPortLeaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("immediate", 1), ("fast", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortLeaveMode.setStatus('current')
zyIgmpSnoopingPortLeaveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortLeaveTimeout.setStatus('current')
zyIgmpSnoopingPortFastLeaveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingPortFastLeaveTimeout.setStatus('current')
zyxelIgmpSnoopingRecordTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingRecordTable.setStatus('current')
zyxelIgmpSnoopingRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordVid"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordPort"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordGroup"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingRecordEntry.setStatus('current')
zyIgmpSnoopingRecordIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingRecordIndex.setStatus('current')
zyIgmpSnoopingRecordVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingRecordVid.setStatus('current')
zyIgmpSnoopingRecordPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingRecordPort.setStatus('current')
zyIgmpSnoopingRecordGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: zyIgmpSnoopingRecordGroup.setStatus('current')
zyIgmpSnoopingRecordTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingRecordTimeout.setStatus('current')
zyIgmpSnoopingRecordUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingRecordUpTime.setStatus('current')
zyxelIgmpSnoopingInfoVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingInfoVlanTable.setStatus('current')
zyxelIgmpSnoopingInfoVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingInfoVlanVid"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingInfoVlanEntry.setStatus('current')
zyIgmpSnoopingInfoVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingInfoVlanVid.setStatus('current')
zyIgmpSnoopingInfoVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dynamic", 1), ("mvr", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingInfoVlanType.setStatus('current')
zyIgmpSnoopingInfoVlanQueryPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingInfoVlanQueryPorts.setStatus('current')
zyxelIgmpSnoopingCountTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountTable.setStatus('current')
zyxelIgmpSnoopingCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingCountIndex"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountEntry.setStatus('current')
zyIgmpSnoopingCountIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingCountIndex.setStatus('current')
zyIgmpSnoopingCountV2QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2QueryRx.setStatus('current')
zyIgmpSnoopingCountV2ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2ReportRx.setStatus('current')
zyIgmpSnoopingCountV2LeaveRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2LeaveRx.setStatus('current')
zyIgmpSnoopingCountV2QueryRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2QueryRxDrop.setStatus('current')
zyIgmpSnoopingCountV2ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountV2LeaveRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2LeaveRxDrop.setStatus('current')
zyIgmpSnoopingCountV2QueryTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2QueryTx.setStatus('current')
zyIgmpSnoopingCountV2ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2ReportTx.setStatus('current')
zyIgmpSnoopingCountV2LeaveTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV2LeaveTx.setStatus('current')
zyIgmpSnoopingCountV3QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3QueryRx.setStatus('current')
zyIgmpSnoopingCountV3ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3ReportRx.setStatus('current')
zyIgmpSnoopingCountV3QueryRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3QueryRxDrop.setStatus('current')
zyIgmpSnoopingCountV3ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountV3QueryTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3QueryTx.setStatus('current')
zyIgmpSnoopingCountV3ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountV3ReportTx.setStatus('current')
zyxelIgmpSnoopingCountVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountVlanTable.setStatus('current')
zyxelIgmpSnoopingCountVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingCountVlanVid"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountVlanEntry.setStatus('current')
zyIgmpSnoopingCountVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanVid.setStatus('current')
zyIgmpSnoopingCountVlanV2QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2QueryRx.setStatus('current')
zyIgmpSnoopingCountVlanV2ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2ReportRx.setStatus('current')
zyIgmpSnoopingCountVlanV2LeaveRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2LeaveRx.setStatus('current')
zyIgmpSnoopingCountVlanV2QueryRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2QueryRxDrop.setStatus('current')
zyIgmpSnoopingCountVlanV2ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountVlanV2LeaveRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2LeaveRxDrop.setStatus('current')
zyIgmpSnoopingCountVlanV2QueryTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2QueryTx.setStatus('current')
zyIgmpSnoopingCountVlanV2ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2ReportTx.setStatus('current')
zyIgmpSnoopingCountVlanV2LeaveTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV2LeaveTx.setStatus('current')
zyIgmpSnoopingCountVlanV3QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3QueryRx.setStatus('current')
zyIgmpSnoopingCountVlanV3ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3ReportRx.setStatus('current')
zyIgmpSnoopingCountVlanV3QueryRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3QueryRxDrop.setStatus('current')
zyIgmpSnoopingCountVlanV3ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountVlanV3QueryTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3QueryTx.setStatus('current')
zyIgmpSnoopingCountVlanV3ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountVlanV3ReportTx.setStatus('current')
zyxelIgmpSnoopingCountPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountPortTable.setStatus('current')
zyxelIgmpSnoopingCountPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingCountPortEntry.setStatus('current')
zyIgmpSnoopingCountPortV2QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2QueryRx.setStatus('current')
zyIgmpSnoopingCountPortV2ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2ReportRx.setStatus('current')
zyIgmpSnoopingCountPortV2LeaveRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2LeaveRx.setStatus('current')
zyIgmpSnoopingCountPortV2ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountPortV2LeaveRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2LeaveRxDrop.setStatus('current')
zyIgmpSnoopingCountPortV2ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2ReportTx.setStatus('current')
zyIgmpSnoopingCountPortV2LeaveTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV2LeaveTx.setStatus('current')
zyIgmpSnoopingCountPortV3QueryRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV3QueryRx.setStatus('current')
zyIgmpSnoopingCountPortV3ReportRx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV3ReportRx.setStatus('current')
zyIgmpSnoopingCountPortV3ReportRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV3ReportRxDrop.setStatus('current')
zyIgmpSnoopingCountPortV3ReportTx = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingCountPortV3ReportTx.setStatus('current')
zyxelIgmpSnoopingGroupCountStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6))
zyIgmpSnoopingGroupCountNumber = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupCountNumber.setStatus('current')
zyxelIgmpSnoopingGroupCountVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupCountVlanTable.setStatus('current')
zyxelIgmpSnoopingGroupCountVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupCountVlanVid"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupCountVlanEntry.setStatus('current')
zyIgmpSnoopingGroupCountVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingGroupCountVlanVid.setStatus('current')
zyIgmpSnoopingGroupCountVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupCountVlanNumber.setStatus('current')
zyxelIgmpSnoopingGroupCountPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupCountPortTable.setStatus('current')
zyxelIgmpSnoopingGroupCountPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupCountPortEntry.setStatus('current')
zyIgmpSnoopingGroupCountPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupCountPortNumber.setStatus('current')
zyxelIgmpSnoopingGroupStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7))
zyxelIgmpSnoopingGroupTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupTable.setStatus('current')
zyxelIgmpSnoopingGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupVid"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupIpAddress"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingGroupEntry.setStatus('current')
zyIgmpSnoopingGroupVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingGroupVid.setStatus('current')
zyIgmpSnoopingGroupIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: zyIgmpSnoopingGroupIpAddress.setStatus('current')
zyIgmpSnoopingGroupPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupPortCount.setStatus('current')
zyIgmpSnoopingGroupPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingGroupPorts.setStatus('current')
zyxelIgmpSnoopingClientTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8), )
if mibBuilder.loadTexts: zyxelIgmpSnoopingClientTable.setStatus('current')
zyxelIgmpSnoopingClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1), ).setIndexNames((0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientVid"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientPort"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientGroupIpAddress"), (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientIpAddress"))
if mibBuilder.loadTexts: zyxelIgmpSnoopingClientEntry.setStatus('current')
zyIgmpSnoopingClientVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingClientVid.setStatus('current')
zyIgmpSnoopingClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 2), Integer32())
if mibBuilder.loadTexts: zyIgmpSnoopingClientPort.setStatus('current')
zyIgmpSnoopingClientGroupIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 3), IpAddress())
if mibBuilder.loadTexts: zyIgmpSnoopingClientGroupIpAddress.setStatus('current')
zyIgmpSnoopingClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 4), IpAddress())
if mibBuilder.loadTexts: zyIgmpSnoopingClientIpAddress.setStatus('current')
zyIgmpSnoopingClientUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIgmpSnoopingClientUpTime.setStatus('current')
zyIgmpSnoopingStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 9), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingStatisticsClear.setStatus('current')
zyIgmpSnoopingStatisticsClearSystem = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 10), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingStatisticsClearSystem.setStatus('current')
zyIgmpSnoopingStatisticsClearPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 11), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingStatisticsClearPort.setStatus('current')
zyIgmpSnoopingStatisticsClearVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 12), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpSnoopingStatisticsClearVlan.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IGMP-SNOOPING-MIB", zyIgmpSnoopingGroupCountVlanVid=zyIgmpSnoopingGroupCountVlanVid, zyxelIgmpSnoopingSetup=zyxelIgmpSnoopingSetup, zyxelIgmpSnoopingInfoVlanTable=zyxelIgmpSnoopingInfoVlanTable, PYSNMP_MODULE_ID=zyxelIgmpSnooping, zyIgmpSnoopingClientUpTime=zyIgmpSnoopingClientUpTime, zyIgmpSnoopingMaxNumberOfVlans=zyIgmpSnoopingMaxNumberOfVlans, zyIgmpSnoopingCountV2ReportRxDrop=zyIgmpSnoopingCountV2ReportRxDrop, zyIgmpSnoopingVlanName=zyIgmpSnoopingVlanName, zyIgmpSnoopingInfoVlanQueryPorts=zyIgmpSnoopingInfoVlanQueryPorts, zyxelIgmpSnoopingPortTable=zyxelIgmpSnoopingPortTable, zyIgmpSnoopingCountVlanV2QueryRxDrop=zyIgmpSnoopingCountVlanV2QueryRxDrop, zyxelIgmpSnoopingCountVlanEntry=zyxelIgmpSnoopingCountVlanEntry, zyIgmpSnoopingCountVlanV3ReportTx=zyIgmpSnoopingCountVlanV3ReportTx, zyIgmpSnoopingRecordPort=zyIgmpSnoopingRecordPort, zyIgmpSnoopingReportProxyState=zyIgmpSnoopingReportProxyState, zyIgmpSnoopingCountPortV3QueryRx=zyIgmpSnoopingCountPortV3QueryRx, zyIgmpSnoopingRecordVid=zyIgmpSnoopingRecordVid, zyIgmpSnooping8021pPriority=zyIgmpSnooping8021pPriority, zyIgmpSnoopingCountV3QueryRxDrop=zyIgmpSnoopingCountV3QueryRxDrop, zyIgmpSnoopingPortLeaveTimeout=zyIgmpSnoopingPortLeaveTimeout, zyxelIgmpSnooping=zyxelIgmpSnooping, zyIgmpSnoopingGroupHostTimeout=zyIgmpSnoopingGroupHostTimeout, zyIgmpSnoopingQuerierModeState=zyIgmpSnoopingQuerierModeState, zyIgmpSnoopingCountPortV2LeaveTx=zyIgmpSnoopingCountPortV2LeaveTx, zyxelIgmpSnoopingGroupCountVlanEntry=zyxelIgmpSnoopingGroupCountVlanEntry, zyIgmpSnoopingClientPort=zyIgmpSnoopingClientPort, zyIgmpSnoopingStatisticsClearPort=zyIgmpSnoopingStatisticsClearPort, zyIgmpSnoopingGroupCountNumber=zyIgmpSnoopingGroupCountNumber, zyIgmpSnoopingCountV3ReportRx=zyIgmpSnoopingCountV3ReportRx, zyxelIgmpSnoopingPortEntry=zyxelIgmpSnoopingPortEntry, zyIgmpSnoopingPortLeaveMode=zyIgmpSnoopingPortLeaveMode, zyxelIgmpSnoopingGroupEntry=zyxelIgmpSnoopingGroupEntry, zyxelIgmpSnoopingGroupStatus=zyxelIgmpSnoopingGroupStatus, zyIgmpSnoopingGroupVid=zyIgmpSnoopingGroupVid, zyIgmpSnoopingStatisticsClear=zyIgmpSnoopingStatisticsClear, zyIgmpSnoopingGroupCountVlanNumber=zyIgmpSnoopingGroupCountVlanNumber, zyxelIgmpSnoopingInfoVlanEntry=zyxelIgmpSnoopingInfoVlanEntry, zyIgmpSnoopingCountPortV2ReportRx=zyIgmpSnoopingCountPortV2ReportRx, zyIgmpSnoopingPortMaxGroupLimitedState=zyIgmpSnoopingPortMaxGroupLimitedState, zyIgmpSnoopingInfoVlanType=zyIgmpSnoopingInfoVlanType, zyIgmpSnoopingVlanVid=zyIgmpSnoopingVlanVid, zyIgmpSnoopingCountV3ReportRxDrop=zyIgmpSnoopingCountV3ReportRxDrop, zyIgmpSnoopingCountVlanV2ReportRxDrop=zyIgmpSnoopingCountVlanV2ReportRxDrop, zyIgmpSnoopingRecordUpTime=zyIgmpSnoopingRecordUpTime, zyxelIgmpSnoopingCountEntry=zyxelIgmpSnoopingCountEntry, zyIgmpSnoopingRecordTimeout=zyIgmpSnoopingRecordTimeout, zyIgmpSnoopingCountVlanV3ReportRx=zyIgmpSnoopingCountVlanV3ReportRx, zyIgmpSnoopingCountV2QueryRx=zyIgmpSnoopingCountV2QueryRx, zyIgmpSnoopingStatisticsClearSystem=zyIgmpSnoopingStatisticsClearSystem, zyIgmpSnoopingVlanRowStatus=zyIgmpSnoopingVlanRowStatus, zyIgmpSnoopingCountVlanV2ReportRx=zyIgmpSnoopingCountVlanV2ReportRx, zyxelIgmpSnoopingRecordEntry=zyxelIgmpSnoopingRecordEntry, zyIgmpSnoopingCountVlanV2LeaveRxDrop=zyIgmpSnoopingCountVlanV2LeaveRxDrop, zyxelIgmpSnoopingGroupTable=zyxelIgmpSnoopingGroupTable, zyIgmpSnoopingCountPortV2ReportTx=zyIgmpSnoopingCountPortV2ReportTx, zyxelIgmpSnoopingCountTable=zyxelIgmpSnoopingCountTable, zyIgmpSnoopingClientVid=zyIgmpSnoopingClientVid, zyIgmpSnoopingCountVlanV3QueryRx=zyIgmpSnoopingCountVlanV3QueryRx, zyIgmpSnoopingCountVlanV3QueryRxDrop=zyIgmpSnoopingCountVlanV3QueryRxDrop, zyIgmpSnoopingCountV2QueryTx=zyIgmpSnoopingCountV2QueryTx, zyIgmpSnoopingVlanMode=zyIgmpSnoopingVlanMode, zyIgmpSnoopingCountV2QueryRxDrop=zyIgmpSnoopingCountV2QueryRxDrop, zyIgmpSnoopingInfoVlanVid=zyIgmpSnoopingInfoVlanVid, zyIgmpSnoopingCountVlanV2LeaveTx=zyIgmpSnoopingCountVlanV2LeaveTx, zyxelIgmpSnoopingVlanTable=zyxelIgmpSnoopingVlanTable, zyIgmpSnoopingCountVlanV2ReportTx=zyIgmpSnoopingCountVlanV2ReportTx, zyIgmpSnoopingClientIpAddress=zyIgmpSnoopingClientIpAddress, zyIgmpSnoopingCountPortV2LeaveRx=zyIgmpSnoopingCountPortV2LeaveRx, zyIgmpSnoopingCountPortV2ReportRxDrop=zyIgmpSnoopingCountPortV2ReportRxDrop, zyIgmpSnoopingCountPortV3ReportRxDrop=zyIgmpSnoopingCountPortV3ReportRxDrop, zyIgmpSnoopingGroupPortCount=zyIgmpSnoopingGroupPortCount, zyxelIgmpSnoopingCountPortTable=zyxelIgmpSnoopingCountPortTable, zyIgmpSnoopingCountV2LeaveRxDrop=zyIgmpSnoopingCountV2LeaveRxDrop, zyIgmpSnoopingCountVlanV2QueryRx=zyIgmpSnoopingCountVlanV2QueryRx, zyIgmpSnoopingCountPortV2LeaveRxDrop=zyIgmpSnoopingCountPortV2LeaveRxDrop, zyIgmpSnoopingCountPortV3ReportTx=zyIgmpSnoopingCountPortV3ReportTx, zyIgmpSnoopingCountVlanV2QueryTx=zyIgmpSnoopingCountVlanV2QueryTx, zyxelIgmpSnoopingVlanEntry=zyxelIgmpSnoopingVlanEntry, zyIgmpSnoopingGroupPorts=zyIgmpSnoopingGroupPorts, zyIgmpSnoopingCountV2ReportTx=zyIgmpSnoopingCountV2ReportTx, zyIgmpSnoopingCountV2ReportRx=zyIgmpSnoopingCountV2ReportRx, zyxelIgmpSnoopingClientTable=zyxelIgmpSnoopingClientTable, zyIgmpSnoopingPortQuerierMode=zyIgmpSnoopingPortQuerierMode, zyxelIgmpSnoopingGroupCountVlanTable=zyxelIgmpSnoopingGroupCountVlanTable, zyIgmpSnoopingCountVlanV3QueryTx=zyIgmpSnoopingCountVlanV3QueryTx, zyIgmpSnoopingCountVlanV2LeaveRx=zyIgmpSnoopingCountVlanV2LeaveRx, zyIgmpSnoopingRecordIndex=zyIgmpSnoopingRecordIndex, zyxelIgmpSnoopingClientEntry=zyxelIgmpSnoopingClientEntry, zyIgmpSnoopingGroupCountPortNumber=zyIgmpSnoopingGroupCountPortNumber, zyxelIgmpSnoopingCountVlanTable=zyxelIgmpSnoopingCountVlanTable, zyIgmpSnoopingCountV2LeaveTx=zyIgmpSnoopingCountV2LeaveTx, zyxelIgmpSnoopingGroupCountPortTable=zyxelIgmpSnoopingGroupCountPortTable, zyxelIgmpSnoopingCountPortEntry=zyxelIgmpSnoopingCountPortEntry, zyxelIgmpSnoopingStatus=zyxelIgmpSnoopingStatus, zyIgmpSnoopingState=zyIgmpSnoopingState, zyIgmpSnoopingRecordGroup=zyIgmpSnoopingRecordGroup, zyIgmpSnoopingCountVlanV3ReportRxDrop=zyIgmpSnoopingCountVlanV3ReportRxDrop, zyIgmpSnoopingCountV2LeaveRx=zyIgmpSnoopingCountV2LeaveRx, zyIgmpSnoopingCountV3QueryRx=zyIgmpSnoopingCountV3QueryRx, zyIgmpSnoopingClientGroupIpAddress=zyIgmpSnoopingClientGroupIpAddress, zyxelIgmpSnoopingRecordTable=zyxelIgmpSnoopingRecordTable, zyxelIgmpSnoopingGroupCountStatus=zyxelIgmpSnoopingGroupCountStatus, zyIgmpSnoopingStatisticsClearVlan=zyIgmpSnoopingStatisticsClearVlan, zyIgmpSnoopingCountPortV2QueryRx=zyIgmpSnoopingCountPortV2QueryRx, zyIgmpSnoopingCountV3QueryTx=zyIgmpSnoopingCountV3QueryTx, zyIgmpSnoopingPortMaxOfGroups=zyIgmpSnoopingPortMaxOfGroups, zyIgmpSnoopingCountVlanVid=zyIgmpSnoopingCountVlanVid, zyIgmpSnoopingPortFastLeaveTimeout=zyIgmpSnoopingPortFastLeaveTimeout, zyIgmpSnoopingCountIndex=zyIgmpSnoopingCountIndex, zyIgmpSnoopingCountPortV3ReportRx=zyIgmpSnoopingCountPortV3ReportRx, zyIgmpSnoopingGroupIpAddress=zyIgmpSnoopingGroupIpAddress, zyxelIgmpSnoopingGroupCountPortEntry=zyxelIgmpSnoopingGroupCountPortEntry, zyIgmpSnoopingPortThrottlingAction=zyIgmpSnoopingPortThrottlingAction, zyIgmpSnoopingCountV3ReportTx=zyIgmpSnoopingCountV3ReportTx)