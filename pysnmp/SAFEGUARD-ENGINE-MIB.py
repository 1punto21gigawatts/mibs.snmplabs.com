#
# PySNMP MIB module SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAFEGUARD-ENGINE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, MibIdentifier, Counter32, Counter64, Unsigned32, ObjectIdentity, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
swSafeGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 19))
if mibBuilder.loadTexts: swSafeGuardMIB.setLastUpdated('200601160000Z')
if mibBuilder.loadTexts: swSafeGuardMIB.setOrganization(' ')
swSafeGuardGblMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 19, 1))
swSafeGuardctrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 19, 2))
swSafeGuardNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 19, 4))
swSafeGuardAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSafeGuardAdminState.setStatus('current')
swSafeGuardRisingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSafeGuardRisingThreshold.setStatus('current')
swSafeGuardFallingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSafeGuardFallingThreshold.setStatus('current')
swSafeGuardAlarmAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSafeGuardAlarmAdminState.setStatus('current')
swSafeGuardCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("exhausted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSafeGuardCurrentStatus.setStatus('current')
swSafeGuardInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSafeGuardInterval.setStatus('current')
swSafeGuardNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1))
swSafeGuardNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0))
swSafeGuardChgToExhausted = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 1)).setObjects(("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus"))
if mibBuilder.loadTexts: swSafeGuardChgToExhausted.setStatus('current')
swSafeGuardChgToNormal = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 2)).setObjects(("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus"))
if mibBuilder.loadTexts: swSafeGuardChgToNormal.setStatus('current')
mibBuilder.exportSymbols("SAFEGUARD-ENGINE-MIB", swSafeGuardChgToExhausted=swSafeGuardChgToExhausted, PYSNMP_MODULE_ID=swSafeGuardMIB, swSafeGuardGblMgmt=swSafeGuardGblMgmt, swSafeGuardMIB=swSafeGuardMIB, swSafeGuardFallingThreshold=swSafeGuardFallingThreshold, swSafeGuardAdminState=swSafeGuardAdminState, swSafeGuardNotifyPrefix=swSafeGuardNotifyPrefix, swSafeGuardctrl=swSafeGuardctrl, swSafeGuardChgToNormal=swSafeGuardChgToNormal, swSafeGuardRisingThreshold=swSafeGuardRisingThreshold, swSafeGuardNotify=swSafeGuardNotify, swSafeGuardInterval=swSafeGuardInterval, swSafeGuardNotification=swSafeGuardNotification, swSafeGuardCurrentStatus=swSafeGuardCurrentStatus, swSafeGuardAlarmAdminState=swSafeGuardAlarmAdminState)