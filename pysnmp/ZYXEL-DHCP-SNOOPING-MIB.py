#
# PySNMP MIB module ZYXEL-DHCP-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DHCP-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Gauge32, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, ObjectIdentity, Unsigned32, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDhcpSnooping = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20))
if mibBuilder.loadTexts: zyxelDhcpSnooping.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDhcpSnooping.setOrganization('Enterprise Solution ZyXEL')
zyxelDhcpSnoopingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1))
zyxelDhcpSnoopingStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2))
zyDhcpSnoopingState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingState.setStatus('current')
zyxelDhcpSnoopingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2), )
if mibBuilder.loadTexts: zyxelDhcpSnoopingVlanTable.setStatus('current')
zyxelDhcpSnoopingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1), ).setIndexNames((0, "ZYXEL-DHCP-SNOOPING-MIB", "zyDhcpSnoopingVlanVid"))
if mibBuilder.loadTexts: zyxelDhcpSnoopingVlanEntry.setStatus('current')
zyDhcpSnoopingVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyDhcpSnoopingVlanVid.setStatus('current')
zyDhcpSnoopingVlanState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingVlanState.setStatus('current')
zyDhcpSnoopingVlanOption82Profile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingVlanOption82Profile.setStatus('current')
zyxelDhcpSnoopingPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3), )
if mibBuilder.loadTexts: zyxelDhcpSnoopingPortTable.setStatus('current')
zyxelDhcpSnoopingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpSnoopingPortEntry.setStatus('current')
zyDhcpSnoopingPortTrustState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingPortTrustState.setStatus('current')
zyDhcpSnoopingPortRate = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingPortRate.setStatus('current')
zyxelDhcpSnoopingDb = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4))
zyDhcpSnoopingDbAbort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDbAbort.setStatus('current')
zyDhcpSnoopingDbWriteDelay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDbWriteDelay.setStatus('current')
zyDhcpSnoopingDbUrl = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDbUrl.setStatus('current')
zyDhcpSnoopingDbUrlRenew = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDbUrlRenew.setStatus('current')
zyxelDhcpSnoopingDhcpVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 5))
zyDhcpSnoopingDhcpVlanVid = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDhcpVlanVid.setStatus('current')
zyDhcpSnoopingMaxNumberOfOption82VlanPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingMaxNumberOfOption82VlanPort.setStatus('current')
zyxelDhcpSnoopingOption82VlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7), )
if mibBuilder.loadTexts: zyxelDhcpSnoopingOption82VlanPortTable.setStatus('current')
zyxelDhcpSnoopingOption82VlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7, 1), ).setIndexNames((0, "ZYXEL-DHCP-SNOOPING-MIB", "zyDhcpSnoopingVlanVid"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpSnoopingOption82VlanPortEntry.setStatus('current')
zyDhcpSnoopingOption82VlanPortProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpSnoopingOption82VlanPortProfile.setStatus('current')
zyDhcpSnoopingDbStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsClear.setStatus('current')
zyxelDhcpSnoopingDbStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2))
zyDhcpSnoopingDbStatisticsAgentRunning = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("read", 1), ("write", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsAgentRunning.setStatus('current')
zyDhcpSnoopingDbStatisticsDelayExpiry = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsDelayExpiry.setStatus('current')
zyDhcpSnoopingDbStatisticsAbortExpiry = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsAbortExpiry.setStatus('current')
zyDhcpSnoopingDbStatisticsLastSuccessTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastSuccessTime.setStatus('current')
zyDhcpSnoopingDbStatisticsLastFailTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastFailTime.setStatus('current')
zyDhcpSnoopingDbStatisticsLastFailReasonType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastFailReasonType.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalAttempt = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalAttempt.setStatus('current')
zyDhcpSnoopingDbStatisticsStartupFail = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsStartupFail.setStatus('current')
zyDhcpSnoopingDbStatisticsSuccessTrans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsSuccessTrans.setStatus('current')
zyDhcpSnoopingDbStatisticsFailTrans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsFailTrans.setStatus('current')
zyDhcpSnoopingDbStatisticsSuccessRead = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsSuccessRead.setStatus('current')
zyDhcpSnoopingDbStatisticsFailRead = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsFailRead.setStatus('current')
zyDhcpSnoopingDbStatisticsSuccessWrite = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsSuccessWrite.setStatus('current')
zyDhcpSnoopingDbStatisticsFailWrite = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsFailWrite.setStatus('current')
zyDhcpSnoopingDbStatisticsFirstSuccessAccess = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("read", 1), ("write", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsFirstSuccessAccess.setStatus('current')
zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision.setStatus('current')
zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease.setStatus('current')
zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface.setStatus('current')
zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan.setStatus('current')
zyDhcpSnoopingDbStatisticsLastIgnoreParse = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsLastIgnoreParse.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan.setStatus('current')
zyDhcpSnoopingDbStatisticsTotalIgnoreParse = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpSnoopingDbStatisticsTotalIgnoreParse.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DHCP-SNOOPING-MIB", zyxelDhcpSnoopingPortEntry=zyxelDhcpSnoopingPortEntry, zyxelDhcpSnoopingVlanTable=zyxelDhcpSnoopingVlanTable, zyDhcpSnoopingDbAbort=zyDhcpSnoopingDbAbort, zyDhcpSnoopingDbStatisticsAbortExpiry=zyDhcpSnoopingDbStatisticsAbortExpiry, zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface=zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface, zyxelDhcpSnoopingStatus=zyxelDhcpSnoopingStatus, zyDhcpSnoopingDbStatisticsSuccessTrans=zyDhcpSnoopingDbStatisticsSuccessTrans, zyxelDhcpSnoopingOption82VlanPortTable=zyxelDhcpSnoopingOption82VlanPortTable, zyDhcpSnoopingDbStatisticsFailWrite=zyDhcpSnoopingDbStatisticsFailWrite, zyxelDhcpSnoopingDb=zyxelDhcpSnoopingDb, zyxelDhcpSnoopingSetup=zyxelDhcpSnoopingSetup, zyDhcpSnoopingOption82VlanPortProfile=zyDhcpSnoopingOption82VlanPortProfile, zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease=zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease, zyDhcpSnoopingDbStatisticsFirstSuccessAccess=zyDhcpSnoopingDbStatisticsFirstSuccessAccess, zyDhcpSnoopingDbStatisticsFailRead=zyDhcpSnoopingDbStatisticsFailRead, zyxelDhcpSnoopingDhcpVlan=zyxelDhcpSnoopingDhcpVlan, zyDhcpSnoopingVlanVid=zyDhcpSnoopingVlanVid, zyDhcpSnoopingDbUrl=zyDhcpSnoopingDbUrl, PYSNMP_MODULE_ID=zyxelDhcpSnooping, zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision=zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision, zyDhcpSnoopingDbStatisticsLastFailTime=zyDhcpSnoopingDbStatisticsLastFailTime, zyxelDhcpSnoopingOption82VlanPortEntry=zyxelDhcpSnoopingOption82VlanPortEntry, zyDhcpSnoopingDbStatisticsTotalAttempt=zyDhcpSnoopingDbStatisticsTotalAttempt, zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan=zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan, zyDhcpSnoopingDbStatisticsAgentRunning=zyDhcpSnoopingDbStatisticsAgentRunning, zyDhcpSnoopingDbStatisticsSuccessRead=zyDhcpSnoopingDbStatisticsSuccessRead, zyDhcpSnoopingDbStatisticsLastIgnoreParse=zyDhcpSnoopingDbStatisticsLastIgnoreParse, zyDhcpSnoopingState=zyDhcpSnoopingState, zyxelDhcpSnoopingVlanEntry=zyxelDhcpSnoopingVlanEntry, zyDhcpSnoopingDbUrlRenew=zyDhcpSnoopingDbUrlRenew, zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease=zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease, zyDhcpSnoopingDbStatisticsLastFailReasonType=zyDhcpSnoopingDbStatisticsLastFailReasonType, zyDhcpSnoopingPortTrustState=zyDhcpSnoopingPortTrustState, zyDhcpSnoopingPortRate=zyDhcpSnoopingPortRate, zyDhcpSnoopingDbStatisticsLastSuccessTime=zyDhcpSnoopingDbStatisticsLastSuccessTime, zyDhcpSnoopingDbStatisticsStartupFail=zyDhcpSnoopingDbStatisticsStartupFail, zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface=zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface, zyxelDhcpSnoopingPortTable=zyxelDhcpSnoopingPortTable, zyDhcpSnoopingDbStatisticsFailTrans=zyDhcpSnoopingDbStatisticsFailTrans, zyxelDhcpSnoopingDbStatistics=zyxelDhcpSnoopingDbStatistics, zyDhcpSnoopingDbStatisticsTotalIgnoreParse=zyDhcpSnoopingDbStatisticsTotalIgnoreParse, zyxelDhcpSnooping=zyxelDhcpSnooping, zyDhcpSnoopingVlanState=zyDhcpSnoopingVlanState, zyDhcpSnoopingMaxNumberOfOption82VlanPort=zyDhcpSnoopingMaxNumberOfOption82VlanPort, zyDhcpSnoopingDbStatisticsClear=zyDhcpSnoopingDbStatisticsClear, zyDhcpSnoopingDbStatisticsDelayExpiry=zyDhcpSnoopingDbStatisticsDelayExpiry, zyDhcpSnoopingDhcpVlanVid=zyDhcpSnoopingDhcpVlanVid, zyDhcpSnoopingDbStatisticsSuccessWrite=zyDhcpSnoopingDbStatisticsSuccessWrite, zyDhcpSnoopingVlanOption82Profile=zyDhcpSnoopingVlanOption82Profile, zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision=zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision, zyDhcpSnoopingDbWriteDelay=zyDhcpSnoopingDbWriteDelay, zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan=zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan)