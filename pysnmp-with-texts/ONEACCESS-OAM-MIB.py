#
# PySNMP MIB module ONEACCESS-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-OAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
atmVclEntry, = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
oacMIBModules, oacExpIMAtmOamStatistics = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMAtmOamStatistics")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, iso, Bits, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Bits", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Integer32", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString, TimeInterval, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeInterval", "TimeStamp")
oacOamMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 673))
oacOamMIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacOamMIBModule.setRevisionsDescriptions(('Fixed Minor correction added last revision.', 'This MIB module describes IP ACL Management objects.',))
if mibBuilder.loadTexts: oacOamMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacOamMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacOamMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacOamMIBModule.setDescription('Contact updated')
oacAtmOamStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1))
oacAtmOamStatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 2))
oacAtmOamStatConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3))
oacAtmOamStatSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1))
oacAtmOamSwitchMaxConnections = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchMaxConnections.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchMaxConnections.setDescription(' Maximum number of authorised OAM configured connections')
oacAtmOamSwitchSegLoopback = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchSegLoopback.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchSegLoopback.setDescription(' Enable segment loopback on this switch')
oacAtmOamSwitchEndLoopback = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchEndLoopback.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchEndLoopback.setDescription(' Enable end to end loopback on this switch')
oacAtmOamSwitchAisRdiEnable = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchAisRdiEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchAisRdiEnable.setDescription(' Enable Remote Defect Indication OAM cell generation if an Alarm Indication Signal OAM cell is received, or if a defect is detected on the switch')
oacAtmOamSwitchSegmentContinuityCheckEnable = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchSegmentContinuityCheckEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchSegmentContinuityCheckEnable.setDescription(' Enable Segment Loss of Continuity cells defect on the pvc. Enable generation of segment Continuity Check cells on the switch.')
oacAtmOamSwitchEndContinuityCheckEnable = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchEndContinuityCheckEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchEndContinuityCheckEnable.setDescription(' Enable End to End Loss of Continuity cells defect on the pvc. Enable generation of End to End Continuity Check cells on the switch.')
oacAtmOamSwitchOamCellsReceived = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchOamCellsReceived.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchOamCellsReceived.setDescription(' Number of received OAM cells on the switch')
oacAtmOamSwitchOamCellsTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchOamCellsTransmitted.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchOamCellsTransmitted.setDescription(' Number of transmitted OAM cells on the switch')
oacAtmOamSwitchCurrentConnections = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamSwitchCurrentConnections.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamSwitchCurrentConnections.setDescription(' Current number of OAM configured connections')
oacAtmOamVclTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2), )
if mibBuilder.loadTexts: oacAtmOamVclTable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclTable.setDescription('An index into the table oacAtmOamVclTable')
oacAtmOamVclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1), )
atmVclEntry.registerAugmentions(("ONEACCESS-OAM-MIB", "oacAtmOamVclEntry"))
oacAtmOamVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
if mibBuilder.loadTexts: oacAtmOamVclEntry.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEntry.setDescription('An index into the table oacAtmOamVclTable')
oacAtmOamVclPvcManage = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclPvcManage.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclPvcManage.setDescription(' Enable OAM for Pvc management')
oacAtmOamVclSegmentLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegmentLoopback.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegmentLoopback.setDescription(' Enable segment loopback on this virtual channel')
oacAtmOamVclEndLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndLoopback.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndLoopback.setDescription(' Enable end to end loopback on this virtual channel')
oacAtmOamVclAisRdiEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAisRdiEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAisRdiEnable.setDescription(' Enable Remote Defect Indication OAM cell generation if an Alarm Indication Signal OAM cell is received, or if a defect is detected on the PVC')
oacAtmOamVclSegmentContinuityCheckEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegmentContinuityCheckEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegmentContinuityCheckEnable.setDescription(' Enable Segment Loss of Continuity cells detect on the PVC.Enable generation of Segment Continuity Check cells on the PVC.')
oacAtmOamVclEndContinuityCheckEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndContinuityCheckEnable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndContinuityCheckEnable.setDescription(' Enable End to End Loss of Continuity cells detect on the PVC.Enable generation of End to End Continuity Check cells on the PVC.')
oacAtmOamVclLoopbackTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxInterval.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxInterval.setDescription(' Frequency of OAM loopback cell are generated on this virtual channel')
oacAtmOamVclLoopbackTxRetryFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryFrequency.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryFrequency.setDescription(' Frequency of OAM loopback cell are generated on this virtual channel, when a change has occured, that is to say either no reception of the last loopback cell, or reception of the last loopback cell')
oacAtmOamVclLoopbackTxRetryUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryUpCount.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryUpCount.setDescription(' Counter of consecutive received loopback cells, before vcl is considered as being up')
oacAtmOamVclLoopbackTxRetryDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryDownCount.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclLoopbackTxRetryDownCount.setDescription(' Counter of consecutive non received loopback cells, before vcl is considered as being down')
oacAtmOamVclAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAlarmState.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAlarmState.setDescription(' This object indicates the current alarm status of the VCL, when error monitoring is activated on the VCL. Value indicates the different alarm states tha the VCL can take. Those alarms can be combined together. The unknown state indicates that the alarm status of this VCL cannot be determined. cc_seg_loc(1),cc_ete_loc(2), lb_seg_alarm(4),lb_ete_alarm(8), ais_alarm(16),rdi_alarm(32),other(64)')
oacAtmOamVclAlarmStateLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAlarmStateLastChange.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAlarmStateLastChange.setDescription(' The value of sysUpTime object at the time this VCL entered its current alarm status. If the current state was entered prior to the last re-initialization of the agent, then this object contains a zero value.')
oacAtmOamVclAisRdiRetryDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAisRdiRetryDownCount.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAisRdiRetryDownCount.setDescription(' Number of consecutive OAM AIS/RDI cells received. The range is 3 to 60. The default is 3.')
oacAtmOamVclAisRdiRetryUpTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAisRdiRetryUpTimer.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAisRdiRetryUpTimer.setDescription(' Number of seconds with no OAM AIS/RDI cells received. The range is 3 to 60 seconds . The default is 3 seconds.')
oacAtmOamVclPvcIntrusive = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclPvcIntrusive.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclPvcIntrusive.setDescription(' Enable OAM Intrusivity against Pvc')
oacAtmOamVclCountersTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3), )
if mibBuilder.loadTexts: oacAtmOamVclCountersTable.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclCountersTable.setDescription('An index into table oacAtmOamVclCountersTable')
oacAtmOamVclCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1), )
atmVclEntry.registerAugmentions(("ONEACCESS-OAM-MIB", "oacAtmOamVclCountersEntry"))
oacAtmOamVclCountersEntry.setIndexNames(*atmVclEntry.getIndexNames())
if mibBuilder.loadTexts: oacAtmOamVclCountersEntry.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclCountersEntry.setDescription('An index into table oacAtmOamVclCountersTable')
oacAtmOamVclOamCellsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclOamCellsReceived.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclOamCellsReceived.setDescription(' Number of received oam cells')
oacAtmOamVclEndLoopbackIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndLoopbackIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndLoopbackIn.setDescription(' Number of received non looped end to end oam loopback cells ')
oacAtmOamVclSegLoopbackIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegLoopbackIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegLoopbackIn.setDescription(' Number of received non looped segment oam loopback cells')
oacAtmOamVclEndLoopIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndLoopIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndLoopIn.setDescription(' Number of received looped end to end oam loopback cells')
oacAtmOamVclSegLoopIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegLoopIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegLoopIn.setDescription(' Number of received looped segment oam loopback cells')
oacAtmOamVclAisIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAisIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAisIn.setDescription(' Number of received oam ais cells')
oacAtmOamVclRdiIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclRdiIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclRdiIn.setDescription(' Number of received oam rdi cells')
oacAtmOamVclSegCCIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegCCIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegCCIn.setDescription(' Number of received oam end to end continuity check cells')
oacAtmOamVclEndCCIn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndCCIn.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndCCIn.setDescription(' Number of received oam segment continuity check cells')
oacAtmOamVclOamCellsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclOamCellsSent.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclOamCellsSent.setDescription(' Number of sent oam cells')
oacAtmOamVclEndLoopbackOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndLoopbackOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndLoopbackOut.setDescription(' Number of sent non looped end to end oam loopback cells ')
oacAtmOamVclSegLoopbackOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegLoopbackOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegLoopbackOut.setDescription(' Number of sent non looped segment oam loopback cells')
oacAtmOamVclEndLoopOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndLoopOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndLoopOut.setDescription(' Number of sent looped end to end oam loopback cells')
oacAtmOamVclSegLoopOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegLoopOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegLoopOut.setDescription(' Number of sent looped segment oam loopback cells')
oacAtmOamVclAisOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclAisOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclAisOut.setDescription(' Number of sent oam ais cells')
oacAtmOamVclRdiOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclRdiOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclRdiOut.setDescription(' Number of sent oam rdi cells')
oacAtmOamVclSegCCOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclSegCCOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclSegCCOut.setDescription(' Number of sent oam end to end continuity check cells')
oacAtmOamVclEndCCOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclEndCCOut.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclEndCCOut.setDescription(' Number of sent oam segment continuity check cells ')
oacAtmOamVclOamCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAtmOamVclOamCellsDropped.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamVclOamCellsDropped.setDescription(' Number of received oam cells that are ignored and dropped')
oacAtmOamStatGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 1))
oacAtmOamStatCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 2))
oacAtmOamStatCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 2, 1)).setObjects(("ONEACCESS-OAM-MIB", "oacAtmOamStatGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacAtmOamStatCompliance = oacAtmOamStatCompliance.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamStatCompliance.setDescription('The compliance statement for agents that support the ONEACCESS-OAM-MIB.')
oacAtmOamStatGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 1, 1)).setObjects(("ONEACCESS-OAM-MIB", "oacAtmOamSwitchMaxConnections"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchSegLoopback"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchEndLoopback"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchAisRdiEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchSegmentContinuityCheckEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchEndContinuityCheckEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchOamCellsReceived"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchOamCellsTransmitted"), ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchCurrentConnections"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclPvcManage"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegmentLoopback"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopback"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegmentContinuityCheckEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndContinuityCheckEnable"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxInterval"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryFrequency"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryUpCount"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryDownCount"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAlarmState"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAlarmStateLastChange"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiRetryDownCount"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiRetryUpTimer"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclPvcIntrusive"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsReceived"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopbackIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopbackIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclRdiIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegCCIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndCCIn"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsSent"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopbackOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopbackOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclRdiOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegCCOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndCCOut"), ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacAtmOamStatGeneralGroup = oacAtmOamStatGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: oacAtmOamStatGeneralGroup.setDescription('This group is mandatory for all OAM entities.')
mibBuilder.exportSymbols("ONEACCESS-OAM-MIB", oacAtmOamVclSegCCOut=oacAtmOamVclSegCCOut, oacAtmOamVclEndLoopback=oacAtmOamVclEndLoopback, oacAtmOamVclLoopbackTxRetryDownCount=oacAtmOamVclLoopbackTxRetryDownCount, oacOamMIBModule=oacOamMIBModule, oacAtmOamVclEndCCOut=oacAtmOamVclEndCCOut, oacAtmOamVclSegLoopbackIn=oacAtmOamVclSegLoopbackIn, oacAtmOamVclOamCellsSent=oacAtmOamVclOamCellsSent, oacAtmOamVclAisRdiRetryDownCount=oacAtmOamVclAisRdiRetryDownCount, oacAtmOamVclEndLoopbackIn=oacAtmOamVclEndLoopbackIn, oacAtmOamVclSegmentLoopback=oacAtmOamVclSegmentLoopback, oacAtmOamVclEndLoopIn=oacAtmOamVclEndLoopIn, oacAtmOamVclRdiOut=oacAtmOamVclRdiOut, oacAtmOamVclAisRdiRetryUpTimer=oacAtmOamVclAisRdiRetryUpTimer, oacAtmOamSwitchSegLoopback=oacAtmOamSwitchSegLoopback, oacAtmOamVclSegmentContinuityCheckEnable=oacAtmOamVclSegmentContinuityCheckEnable, oacAtmOamStatSwitch=oacAtmOamStatSwitch, oacAtmOamVclAlarmState=oacAtmOamVclAlarmState, oacAtmOamVclOamCellsDropped=oacAtmOamVclOamCellsDropped, oacAtmOamVclAisRdiEnable=oacAtmOamVclAisRdiEnable, oacAtmOamStatCompliances=oacAtmOamStatCompliances, oacAtmOamStatGeneralGroup=oacAtmOamStatGeneralGroup, oacAtmOamSwitchAisRdiEnable=oacAtmOamSwitchAisRdiEnable, oacAtmOamVclAisIn=oacAtmOamVclAisIn, oacAtmOamVclEndLoopOut=oacAtmOamVclEndLoopOut, oacAtmOamStatGroups=oacAtmOamStatGroups, oacAtmOamVclAisOut=oacAtmOamVclAisOut, PYSNMP_MODULE_ID=oacOamMIBModule, oacAtmOamVclSegCCIn=oacAtmOamVclSegCCIn, oacAtmOamVclPvcManage=oacAtmOamVclPvcManage, oacAtmOamSwitchOamCellsReceived=oacAtmOamSwitchOamCellsReceived, oacAtmOamVclSegLoopOut=oacAtmOamVclSegLoopOut, oacAtmOamStatCompliance=oacAtmOamStatCompliance, oacAtmOamVclEndCCIn=oacAtmOamVclEndCCIn, oacAtmOamSwitchSegmentContinuityCheckEnable=oacAtmOamSwitchSegmentContinuityCheckEnable, oacAtmOamVclLoopbackTxInterval=oacAtmOamVclLoopbackTxInterval, oacAtmOamVclOamCellsReceived=oacAtmOamVclOamCellsReceived, oacAtmOamStatObjects=oacAtmOamStatObjects, oacAtmOamVclEndLoopbackOut=oacAtmOamVclEndLoopbackOut, oacAtmOamVclLoopbackTxRetryFrequency=oacAtmOamVclLoopbackTxRetryFrequency, oacAtmOamVclAlarmStateLastChange=oacAtmOamVclAlarmStateLastChange, oacAtmOamStatConformance=oacAtmOamStatConformance, oacAtmOamSwitchEndContinuityCheckEnable=oacAtmOamSwitchEndContinuityCheckEnable, oacAtmOamVclCountersEntry=oacAtmOamVclCountersEntry, oacAtmOamSwitchEndLoopback=oacAtmOamSwitchEndLoopback, oacAtmOamVclEndContinuityCheckEnable=oacAtmOamVclEndContinuityCheckEnable, oacAtmOamVclCountersTable=oacAtmOamVclCountersTable, oacAtmOamSwitchOamCellsTransmitted=oacAtmOamSwitchOamCellsTransmitted, oacAtmOamVclRdiIn=oacAtmOamVclRdiIn, oacAtmOamVclTable=oacAtmOamVclTable, oacAtmOamVclEntry=oacAtmOamVclEntry, oacAtmOamSwitchMaxConnections=oacAtmOamSwitchMaxConnections, oacAtmOamVclLoopbackTxRetryUpCount=oacAtmOamVclLoopbackTxRetryUpCount, oacAtmOamSwitchCurrentConnections=oacAtmOamSwitchCurrentConnections, oacAtmOamVclPvcIntrusive=oacAtmOamVclPvcIntrusive, oacAtmOamVclSegLoopbackOut=oacAtmOamVclSegLoopbackOut, oacAtmOamVclSegLoopIn=oacAtmOamVclSegLoopIn, oacAtmOamStatNotifications=oacAtmOamStatNotifications)