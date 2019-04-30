#
# PySNMP MIB module HPN-ICF-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-USER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, Integer32, Counter64, iso, ObjectIdentity, Unsigned32, Bits, TimeTicks, Gauge32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "Integer32", "Counter64", "iso", "ObjectIdentity", "Unsigned32", "Bits", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention, DateAndTime, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "MacAddress", "RowStatus")
hpnicfUser = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12))
if mibBuilder.loadTexts: hpnicfUser.setLastUpdated('201210110000Z')
if mibBuilder.loadTexts: hpnicfUser.setOrganization('')
class ServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

hpnicfUserObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1))
hpnicfUserInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1), )
if mibBuilder.loadTexts: hpnicfUserInfoTable.setStatus('current')
hpnicfUserInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"))
if mibBuilder.loadTexts: hpnicfUserInfoEntry.setStatus('current')
hpnicfUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserName.setStatus('current')
hpnicfUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserPassword.setStatus('current')
hpnicfAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfAuthMode.setStatus('current')
hpnicfUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserLevel.setStatus('current')
hpnicfUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("block", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserState.setStatus('current')
hpnicfUserInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserInfoRowStatus.setStatus('current')
hpnicfUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483646)))
if mibBuilder.loadTexts: hpnicfUserIndex.setStatus('current')
hpnicfUserAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2), )
if mibBuilder.loadTexts: hpnicfUserAttributeTable.setStatus('current')
hpnicfUserAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"))
if mibBuilder.loadTexts: hpnicfUserAttributeEntry.setStatus('current')
hpnicfAccessLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfAccessLimit.setStatus('current')
hpnicfIdleCut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIdleCut.setStatus('current')
hpnicfIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIPAddress.setStatus('current')
hpnicfNasIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNasIPAddress.setStatus('current')
hpnicfSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSlotNum.setStatus('current')
hpnicfSubSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSubSlotNum.setStatus('current')
hpnicfPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPortNum.setStatus('current')
hpnicfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMacAddress.setStatus('current')
hpnicfVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfVlan.setStatus('current')
hpnicfFtpService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 10), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFtpService.setStatus('current')
hpnicfFtpDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFtpDirectory.setStatus('current')
hpnicfLanAccessService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 12), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfLanAccessService.setStatus('current')
hpnicfSshService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 13), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSshService.setStatus('current')
hpnicfTelnetService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 14), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfTelnetService.setStatus('current')
hpnicfTerminalService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 15), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfTerminalService.setStatus('current')
hpnicfExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 16), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfExpirationDate.setStatus('current')
hpnicfUserGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUserGroup.setStatus('current')
hpnicfPortalService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 18), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPortalService.setStatus('current')
hpnicfPPPService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 19), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPPPService.setStatus('current')
hpnicfHttpService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 20), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfHttpService.setStatus('current')
hpnicfHttpsService = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 21), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfHttpsService.setStatus('current')
hpnicfUserIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUserIfIndex.setStatus('current')
hpnicfUserMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUserMaxNum.setStatus('current')
hpnicfUserCurrNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUserCurrNum.setStatus('current')
hpnicfUserIndexIndicator = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUserIndexIndicator.setStatus('current')
hpnicfUserRoleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6), )
if mibBuilder.loadTexts: hpnicfUserRoleTable.setStatus('current')
hpnicfUserRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"), (0, "HPN-ICF-USER-MIB", "hpnicfUserRole"))
if mibBuilder.loadTexts: hpnicfUserRoleEntry.setStatus('current')
hpnicfUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63)))
if mibBuilder.loadTexts: hpnicfUserRole.setStatus('current')
hpnicfUserRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserRoleStatus.setStatus('current')
hpnicfUserGroupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2))
hpnicfUserGroupInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1), )
if mibBuilder.loadTexts: hpnicfUserGroupInfoTable.setStatus('current')
hpnicfUserGroupInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-USER-MIB", "hpnicfUserGroupName"))
if mibBuilder.loadTexts: hpnicfUserGroupInfoEntry.setStatus('current')
hpnicfUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: hpnicfUserGroupName.setStatus('current')
hpnicfUserGroupInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfUserGroupInfoRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-USER-MIB", hpnicfUserRoleEntry=hpnicfUserRoleEntry, hpnicfUserGroupName=hpnicfUserGroupName, hpnicfIdleCut=hpnicfIdleCut, hpnicfFtpDirectory=hpnicfFtpDirectory, hpnicfUserInfoTable=hpnicfUserInfoTable, hpnicfSlotNum=hpnicfSlotNum, hpnicfPortalService=hpnicfPortalService, hpnicfIPAddress=hpnicfIPAddress, hpnicfUserIfIndex=hpnicfUserIfIndex, hpnicfUserCurrNum=hpnicfUserCurrNum, hpnicfUser=hpnicfUser, hpnicfExpirationDate=hpnicfExpirationDate, ServiceType=ServiceType, hpnicfUserInfoRowStatus=hpnicfUserInfoRowStatus, hpnicfHttpService=hpnicfHttpService, hpnicfUserRoleTable=hpnicfUserRoleTable, hpnicfUserIndexIndicator=hpnicfUserIndexIndicator, hpnicfUserLevel=hpnicfUserLevel, hpnicfUserName=hpnicfUserName, hpnicfUserGroupInfoTable=hpnicfUserGroupInfoTable, hpnicfFtpService=hpnicfFtpService, hpnicfNasIPAddress=hpnicfNasIPAddress, hpnicfUserAttributeTable=hpnicfUserAttributeTable, hpnicfUserAttributeEntry=hpnicfUserAttributeEntry, hpnicfAuthMode=hpnicfAuthMode, hpnicfPPPService=hpnicfPPPService, hpnicfTelnetService=hpnicfTelnetService, hpnicfUserObjects=hpnicfUserObjects, hpnicfSshService=hpnicfSshService, hpnicfUserIndex=hpnicfUserIndex, hpnicfUserGroup=hpnicfUserGroup, hpnicfUserState=hpnicfUserState, hpnicfAccessLimit=hpnicfAccessLimit, hpnicfMacAddress=hpnicfMacAddress, PYSNMP_MODULE_ID=hpnicfUser, hpnicfVlan=hpnicfVlan, hpnicfTerminalService=hpnicfTerminalService, hpnicfUserPassword=hpnicfUserPassword, hpnicfSubSlotNum=hpnicfSubSlotNum, hpnicfUserRoleStatus=hpnicfUserRoleStatus, hpnicfUserMaxNum=hpnicfUserMaxNum, hpnicfPortNum=hpnicfPortNum, hpnicfUserGroupInfoEntry=hpnicfUserGroupInfoEntry, hpnicfHttpsService=hpnicfHttpsService, hpnicfUserGroupObjects=hpnicfUserGroupObjects, hpnicfUserInfoEntry=hpnicfUserInfoEntry, hpnicfLanAccessService=hpnicfLanAccessService, hpnicfUserRole=hpnicfUserRole, hpnicfUserGroupInfoRowStatus=hpnicfUserGroupInfoRowStatus)