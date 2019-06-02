#
# PySNMP MIB module A3COM0039-GENERIC-BRIDGE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0039-GENERIC-BRIDGE
# Produced by pysmi-0.3.4 at Wed May  1 11:08:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bridgeMgmt, = mibBuilder.importSymbols("A3COM0004-GENERIC", "bridgeMgmt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, IpAddress, MibIdentifier, Unsigned32, ObjectIdentity, Integer32, NotificationType, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brControlPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 1))
brClearCounters = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-action", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brClearCounters.setStatus('mandatory')
if mibBuilder.loadTexts: brClearCounters.setDescription('Clears all the counters associated with the bridgeing function for all bridge ports. A read will always return a value of no-action(1), a write of no-acti on(1) will have no effect, while a write of clear(2) will clear all the counters.')
brSTAPMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brSTAPMode.setStatus('mandatory')
if mibBuilder.loadTexts: brSTAPMode.setDescription('Determines whether the STAP algorithm is on or off. The value on(2) provides STAP per Vlan while the value single(3) provides a single STAP domain which runs under the Vlans.')
brLearnMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brLearnMode.setStatus('mandatory')
if mibBuilder.loadTexts: brLearnMode.setDescription('Determines whether the bridge is not learning addresses (off), or learning addresses as permanent, deleteOnReset or deleteOnTimeout.')
brAgingMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brAgingMode.setStatus('mandatory')
if mibBuilder.loadTexts: brAgingMode.setDescription('Determines whether the bridge will age out entries in its filtering database or not.')
brMonitorPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 2))
brDataBase = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 4))
brDummyPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 5))
brDatabaseType = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("filtering", 1), ("permanent", 2), ("atmCam", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brDatabaseType.setStatus('mandatory')
if mibBuilder.loadTexts: brDatabaseType.setDescription('This dummy object enables the database full trap to differentiate between the filtering database, the permanent database and the ATM CAM.')
brDatabaseLevel = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(90, 100))).clone(namedValues=NamedValues(("ninetyPercent", 90), ("oneHundredPercent", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brDatabaseLevel.setStatus('mandatory')
if mibBuilder.loadTexts: brDatabaseLevel.setDescription('This dummy object enables the database full trap to differentiate between the database being 90% and 100% full.')
mibBuilder.exportSymbols("A3COM0039-GENERIC-BRIDGE", brClearCounters=brClearCounters, brDataBase=brDataBase, brLearnMode=brLearnMode, brControlPackage=brControlPackage, brDatabaseType=brDatabaseType, brAgingMode=brAgingMode, brSTAPMode=brSTAPMode, brDummyPackage=brDummyPackage, brMonitorPackage=brMonitorPackage, brDatabaseLevel=brDatabaseLevel)