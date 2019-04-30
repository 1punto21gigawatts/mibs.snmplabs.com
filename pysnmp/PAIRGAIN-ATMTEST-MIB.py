#
# PySNMP MIB module PAIRGAIN-ATMTEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-ATMTEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, TimeTicks, MibIdentifier, Counter64, Counter32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, iso, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Counter32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "iso", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
pgATMTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 9))
if mibBuilder.loadTexts: pgATMTestMIB.setLastUpdated('9605010000Z')
if mibBuilder.loadTexts: pgATMTestMIB.setOrganization('PairGain Technologies.')
pgATMTestMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1))
pgoamLoopbackAddress = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16).clone(hexValue="ffffffffffffffff")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgoamLoopbackAddress.setStatus('current')
pgoamLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2), )
if mibBuilder.loadTexts: pgoamLoopbackTable.setStatus('current')
pgoamLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1), ).setIndexNames((0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"), (0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"), (0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"))
if mibBuilder.loadTexts: pgoamLoopbackEntry.setStatus('current')
pgoamLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackIfIndex.setStatus('current')
pgoamLoopbackVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackVpi.setStatus('current')
pgoamLoopbackVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackVci.setStatus('current')
pgoamLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("segment", 1), ("end2end", 2))).clone('segment')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackType.setStatus('current')
pgoamLoopbackLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16).clone(hexValue="ffffffffffffffff")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackLocation.setStatus('current')
pgoamLoopbackCount = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackCount.setStatus('current')
pgoamLoopbackTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 15)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackTimeout.setStatus('current')
pgoamLoopbackDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 15)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackDelay.setStatus('current')
pgoamLoopbackTrapOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackTrapOnCompletion.setStatus('current')
pgoamLoopbackSentCells = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackSentCells.setStatus('current')
pgoamLoopbackReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackReceivedCells.setStatus('current')
pgoamLoopbackErroredCells = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackErroredCells.setStatus('current')
pgoamLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("null", 1), ("inProgress", 2), ("completed", 3), ("aborted", 4), ("failed", 5), ("expired", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgoamLoopbackStatus.setStatus('current')
pgoamLoopbackEntryOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 15), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackEntryOwner.setStatus('current')
pgoamLoopbackEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgoamLoopbackEntryStatus.setStatus('current')
pgoamLoopbackFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oamF4", 1), ("oamF5", 2))).clone('oamF5')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgoamLoopbackFlowType.setStatus('current')
pgATMTestMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2))
pgoamLoopbackMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2, 0))
pgoamLoopbackCompletionTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2, 0, 1)).setObjects(("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackStatus"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackSentCells"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackReceivedCells"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackErroredCells"))
if mibBuilder.loadTexts: pgoamLoopbackCompletionTrap.setStatus('current')
pgATMTestMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3))
pgATMTestMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 1))
pgATMTestMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 2))
pgATMTestMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 1, 1)).setObjects(("PAIRGAIN-ATMTEST-MIB", "pgATMTestMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pgATMTestMIBCompliance = pgATMTestMIBCompliance.setStatus('current')
pgATMTestMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 2, 1)).setObjects(("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackCount"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackType"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackLocation"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackTimeout"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackDelay"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackTrapOnCompletion"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackSentCells"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackReceivedCells"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackErroredCells"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackStatus"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackEntryOwner"), ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pgATMTestMIBGroup = pgATMTestMIBGroup.setStatus('current')
mibBuilder.exportSymbols("PAIRGAIN-ATMTEST-MIB", pgoamLoopbackType=pgoamLoopbackType, pgoamLoopbackCount=pgoamLoopbackCount, pgATMTestMIBGroup=pgATMTestMIBGroup, pgATMTestMIBGroups=pgATMTestMIBGroups, pgoamLoopbackFlowType=pgoamLoopbackFlowType, pgoamLoopbackAddress=pgoamLoopbackAddress, pgoamLoopbackReceivedCells=pgoamLoopbackReceivedCells, pgoamLoopbackTrapOnCompletion=pgoamLoopbackTrapOnCompletion, PYSNMP_MODULE_ID=pgATMTestMIB, pgATMTestMIBCompliances=pgATMTestMIBCompliances, pgoamLoopbackEntry=pgoamLoopbackEntry, pgoamLoopbackSentCells=pgoamLoopbackSentCells, pgATMTestMIBObjects=pgATMTestMIBObjects, pgATMTestMIB=pgATMTestMIB, pgoamLoopbackDelay=pgoamLoopbackDelay, pgoamLoopbackLocation=pgoamLoopbackLocation, pgoamLoopbackIfIndex=pgoamLoopbackIfIndex, pgoamLoopbackVci=pgoamLoopbackVci, pgATMTestMIBConformance=pgATMTestMIBConformance, pgoamLoopbackStatus=pgoamLoopbackStatus, pgoamLoopbackTable=pgoamLoopbackTable, pgoamLoopbackCompletionTrap=pgoamLoopbackCompletionTrap, pgoamLoopbackErroredCells=pgoamLoopbackErroredCells, pgATMTestMIBCompliance=pgATMTestMIBCompliance, pgoamLoopbackMIBTraps=pgoamLoopbackMIBTraps, pgoamLoopbackEntryStatus=pgoamLoopbackEntryStatus, pgoamLoopbackTimeout=pgoamLoopbackTimeout, pgoamLoopbackVpi=pgoamLoopbackVpi, pgATMTestMIBTrapPrefix=pgATMTestMIBTrapPrefix, pgoamLoopbackEntryOwner=pgoamLoopbackEntryOwner)