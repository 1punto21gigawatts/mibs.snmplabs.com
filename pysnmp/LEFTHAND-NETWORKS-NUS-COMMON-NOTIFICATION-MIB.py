#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonEvents, lhnNusCommonGroups, lhnNusCommonNotification = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonEvents", "lhnNusCommonGroups", "lhnNusCommonNotification")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, TimeTicks, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, NotificationType, ObjectIdentity, Counter32, iso, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "TimeTicks", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "NotificationType", "ObjectIdentity", "Counter32", "iso", "IpAddress", "Integer32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lhnNusCommonNotificationModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 15))
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setLastUpdated('0206250000Z')
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setOrganization('LeftHand Networks, Inc.')
notificationMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessageCount.setStatus('current')
notificationMessageTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2), )
if mibBuilder.loadTexts: notificationMessageTable.setStatus('current')
notificationMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationIndex"))
if mibBuilder.loadTexts: notificationMessageEntry.setStatus('current')
notificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationIndex.setStatus('current')
notificationMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessage.setStatus('current')
notificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationTime.setStatus('current')
userNotification = NotificationType((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationMessage"))
if mibBuilder.loadTexts: userNotification.setStatus('current')
lhnNusCommonEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 2)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "userNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonEventGroup = lhnNusCommonEventGroup.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", notificationMessageEntry=notificationMessageEntry, notificationTime=notificationTime, notificationMessage=notificationMessage, lhnNusCommonEventGroup=lhnNusCommonEventGroup, PYSNMP_MODULE_ID=lhnNusCommonNotificationModule, lhnNusCommonNotificationModule=lhnNusCommonNotificationModule, notificationMessageTable=notificationMessageTable, notificationMessageCount=notificationMessageCount, userNotification=userNotification, notificationIndex=notificationIndex)