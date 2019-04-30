#
# PySNMP MIB module ONEACCESS-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:24:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
oacExpIMManagement, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Bits, Counter32, Counter64, Gauge32, Integer32, iso, NotificationType, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "iso", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
RowStatus, DisplayString, TextualConvention, TruthValue, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue", "PhysAddress")
oacAAAConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 690))
oacAAAConfigMIB.setRevisions(('2011-07-26 00:00', '2011-06-15 00:00', '2010-12-17 00:01', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacAAAConfigMIB.setLastUpdated('201107260000Z')
if mibBuilder.loadTexts: oacAAAConfigMIB.setOrganization(' OneAccess ')
oacAAAConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10))
oacAAAConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1))
oacAAAConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2))
oacAAARadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1), )
if mibBuilder.loadTexts: oacAAARadiusServerConfigTable.setStatus('current')
oacAAARadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAARadiusServerInfo"), (0, "ONEACCESS-AAA-MIB", "oacAAARadiusServerPort"))
if mibBuilder.loadTexts: oacAAARadiusServerConfigEntry.setStatus('current')
oacAAARadiusServerInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerInfo.setStatus('current')
oacAAARadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerPort.setStatus('current')
oacAAARadiusServerSharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerSharedKey.setStatus('current')
oacAAARadiusServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerRetries.setStatus('current')
oacAAARadiusServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerTimeout.setStatus('current')
oacAAARadiusServerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 6), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerInterface.setStatus('current')
oacAAARadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAARadiusServerRowStatus.setStatus('current')
oacAAARadiusConfigAccPort = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacAAARadiusConfigAccPort.setStatus('current')
oacAAATacacsServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3), )
if mibBuilder.loadTexts: oacAAATacacsServerConfigTable.setStatus('current')
oacAAATacacsServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAATacacsServerInfo"), (0, "ONEACCESS-AAA-MIB", "oacAAATacacsServerPort"))
if mibBuilder.loadTexts: oacAAATacacsServerConfigEntry.setStatus('current')
oacAAATacacsServerInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerInfo.setStatus('current')
oacAAATacacsServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(49)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerPort.setStatus('current')
oacAAATacacsServerSharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerSharedKey.setStatus('current')
oacAAATacacsServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerTimeout.setStatus('current')
oacAAATacacsServerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerInterface.setStatus('current')
oacAAATacacsServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAATacacsServerRowStatus.setStatus('current')
oacAAATacacsConfigUseUsername = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacAAATacacsConfigUseUsername.setStatus('current')
oacAAAAuthenticationServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5), )
if mibBuilder.loadTexts: oacAAAAuthenticationServerConfigTable.setStatus('current')
oacAAAAuthenticationServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationFeature"), (0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationReqSrc"))
if mibBuilder.loadTexts: oacAAAAuthenticationServerConfigEntry.setStatus('current')
oacAAAAuthenticationFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("login", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationFeature.setStatus('current')
oacAAAAuthenticationReqSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("console", 2), ("network", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationReqSrc.setStatus('current')
oacAAAAuthenticationSvrType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationSvrType.setStatus('current')
oacAAAAuthenticationServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationServerRowStatus.setStatus('current')
oacAAAAuthenticationConfigBannerSeqTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6), )
if mibBuilder.loadTexts: oacAAAAuthenticationConfigBannerSeqTable.setStatus('current')
oacAAAAuthenticationConfigBannerSeqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAAAuthenticationBannerSequence"))
if mibBuilder.loadTexts: oacAAAAuthenticationConfigBannerSeqEntry.setStatus('current')
oacAAAAuthenticationBannerSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationBannerSequence.setStatus('current')
oacAAAAuthenticationBannerString = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationBannerString.setStatus('current')
oacAAAAuthenticationBannerSeqRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAuthenticationBannerSeqRowStatus.setStatus('current')
oacAAAGroupServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7), )
if mibBuilder.loadTexts: oacAAAGroupServerConfigTable.setStatus('current')
oacAAAGroupServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAAServerGroupName"))
if mibBuilder.loadTexts: oacAAAGroupServerConfigEntry.setStatus('current')
oacAAAServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAServerGroupName.setStatus('current')
oacAAAServerGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("radius", 1), ("tacacs", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAServerGroupType.setStatus('current')
oacAAAServerGroupServerInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAServerGroupServerInfo.setStatus('current')
oacAAAServerGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAServerGroupRowStatus.setStatus('current')
oacAAAAuthorizationConfigCmdLevelDefTacacs = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacAAAAuthorizationConfigCmdLevelDefTacacs.setStatus('current')
oacAAAAccCmdsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9), )
if mibBuilder.loadTexts: oacAAAAccCmdsConfigTable.setStatus('current')
oacAAAAccCmdsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1), ).setIndexNames((0, "ONEACCESS-AAA-MIB", "oacAAAAccCmdAccessLevel"))
if mibBuilder.loadTexts: oacAAAAccCmdsConfigEntry.setStatus('current')
oacAAAAccCmdAccessLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAccCmdAccessLevel.setStatus('current')
oacAAAAccTacacsGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAccTacacsGroupName.setStatus('current')
oacAAAAccCmdsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 9, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacAAAAccCmdsRowStatus.setStatus('current')
oacAAAAccConfigExecStartStop = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacAAAAccConfigExecStartStop.setStatus('current')
oacAAAAccConfigSystemStartStop = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacAAAAccConfigSystemStartStop.setStatus('current')
oacAAAConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 1))
oacAAAConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 1, 1)).setObjects(("ONEACCESS-AAA-MIB", "oacAAAAccConfigSystemStartStop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacAAAConfigGroup = oacAAAConfigGroup.setStatus('current')
oacAAACompls = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 10, 2, 2))
mibBuilder.exportSymbols("ONEACCESS-AAA-MIB", oacAAARadiusConfigAccPort=oacAAARadiusConfigAccPort, oacAAARadiusServerTimeout=oacAAARadiusServerTimeout, oacAAAAuthenticationConfigBannerSeqTable=oacAAAAuthenticationConfigBannerSeqTable, oacAAATacacsServerConfigEntry=oacAAATacacsServerConfigEntry, oacAAATacacsServerPort=oacAAATacacsServerPort, oacAAAAuthenticationServerConfigEntry=oacAAAAuthenticationServerConfigEntry, oacAAARadiusServerRowStatus=oacAAARadiusServerRowStatus, oacAAAAuthenticationServerConfigTable=oacAAAAuthenticationServerConfigTable, PYSNMP_MODULE_ID=oacAAAConfigMIB, oacAAATacacsConfigUseUsername=oacAAATacacsConfigUseUsername, oacAAATacacsServerInfo=oacAAATacacsServerInfo, oacAAARadiusServerRetries=oacAAARadiusServerRetries, oacAAAServerGroupRowStatus=oacAAAServerGroupRowStatus, oacAAAConfigObjects=oacAAAConfigObjects, oacAAAConfigGroup=oacAAAConfigGroup, oacAAACompls=oacAAACompls, oacAAAAccTacacsGroupName=oacAAAAccTacacsGroupName, oacAAATacacsServerRowStatus=oacAAATacacsServerRowStatus, oacAAATacacsServerInterface=oacAAATacacsServerInterface, oacAAARadiusServerConfigEntry=oacAAARadiusServerConfigEntry, oacAAARadiusServerInfo=oacAAARadiusServerInfo, oacAAAGroupServerConfigTable=oacAAAGroupServerConfigTable, oacAAATacacsServerSharedKey=oacAAATacacsServerSharedKey, oacAAAAuthenticationBannerSeqRowStatus=oacAAAAuthenticationBannerSeqRowStatus, oacAAAAccCmdsConfigEntry=oacAAAAccCmdsConfigEntry, oacAAAAccCmdsConfigTable=oacAAAAccCmdsConfigTable, oacAAARadiusServerPort=oacAAARadiusServerPort, oacAAAConfigMIB=oacAAAConfigMIB, oacAAAServerGroupType=oacAAAServerGroupType, oacAAAAuthenticationBannerString=oacAAAAuthenticationBannerString, oacAAAAccConfigExecStartStop=oacAAAAccConfigExecStartStop, oacAAARadiusServerSharedKey=oacAAARadiusServerSharedKey, oacAAAAccConfigSystemStartStop=oacAAAAccConfigSystemStartStop, oacAAAAuthenticationServerRowStatus=oacAAAAuthenticationServerRowStatus, oacAAAConfigGroups=oacAAAConfigGroups, oacAAATacacsServerTimeout=oacAAATacacsServerTimeout, oacAAAAuthenticationReqSrc=oacAAAAuthenticationReqSrc, oacAAARadiusServerInterface=oacAAARadiusServerInterface, oacAAAAuthorizationConfigCmdLevelDefTacacs=oacAAAAuthorizationConfigCmdLevelDefTacacs, oacAAAAccCmdsRowStatus=oacAAAAccCmdsRowStatus, oacAAAAuthenticationBannerSequence=oacAAAAuthenticationBannerSequence, oacAAAConfigConformance=oacAAAConfigConformance, oacAAAAccCmdAccessLevel=oacAAAAccCmdAccessLevel, oacAAAConfig=oacAAAConfig, oacAAATacacsServerConfigTable=oacAAATacacsServerConfigTable, oacAAAServerGroupServerInfo=oacAAAServerGroupServerInfo, oacAAAAuthenticationFeature=oacAAAAuthenticationFeature, oacAAAGroupServerConfigEntry=oacAAAGroupServerConfigEntry, oacAAARadiusServerConfigTable=oacAAARadiusServerConfigTable, oacAAAServerGroupName=oacAAAServerGroupName, oacAAAAuthenticationSvrType=oacAAAAuthenticationSvrType, oacAAAAuthenticationConfigBannerSeqEntry=oacAAAAuthenticationConfigBannerSeqEntry)