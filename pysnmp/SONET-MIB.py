#
# PySNMP MIB module SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter64, ObjectIdentity, transmission, Bits, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter64", "ObjectIdentity", "transmission", "Bits", "IpAddress", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 39))
if mibBuilder.loadTexts: sonetMIB.setLastUpdated('9401030000Z')
if mibBuilder.loadTexts: sonetMIB.setOrganization('IETF AToM MIB Working Group')
sonetObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1))
sonetObjectsPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2))
sonetObjectsVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3))
sonetMedium = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 1))
sonetSection = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 2))
sonetLine = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 3))
sonetFarEndLine = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 4))
sonetPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2, 1))
sonetFarEndPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2, 2))
sonetVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3, 1))
sonetFarEndVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3, 2))
sonetMediumTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1), )
if mibBuilder.loadTexts: sonetMediumTable.setStatus('current')
sonetMediumEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetMediumEntry.setStatus('current')
sonetMediumType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumType.setStatus('current')
sonetMediumTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumTimeElapsed.setStatus('current')
sonetMediumValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumValidIntervals.setStatus('current')
sonetMediumLineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sonetMediumOther", 1), ("sonetMediumB3ZS", 2), ("sonetMediumCMI", 3), ("sonetMediumNRZ", 4), ("sonetMediumRZ", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumLineCoding.setStatus('current')
sonetMediumLineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("sonetOther", 1), ("sonetShortSingleMode", 2), ("sonetLongSingleMode", 3), ("sonetMultiMode", 4), ("sonetCoax", 5), ("sonetUTP", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumLineType.setStatus('current')
sonetMediumCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetMediumCircuitIdentifier.setStatus('current')
sonetSectionCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1), )
if mibBuilder.loadTexts: sonetSectionCurrentTable.setStatus('current')
sonetSectionCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetSectionCurrentEntry.setStatus('current')
sonetSectionCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionCurrentStatus.setStatus('current')
sonetSectionCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionCurrentESs.setStatus('current')
sonetSectionCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionCurrentSESs.setStatus('current')
sonetSectionCurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionCurrentSEFSs.setStatus('current')
sonetSectionCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionCurrentCVs.setStatus('current')
sonetSectionIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2), )
if mibBuilder.loadTexts: sonetSectionIntervalTable.setStatus('current')
sonetSectionIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetSectionIntervalNumber"))
if mibBuilder.loadTexts: sonetSectionIntervalEntry.setStatus('current')
sonetSectionIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetSectionIntervalNumber.setStatus('current')
sonetSectionIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionIntervalESs.setStatus('current')
sonetSectionIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionIntervalSESs.setStatus('current')
sonetSectionIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionIntervalSEFSs.setStatus('current')
sonetSectionIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionIntervalCVs.setStatus('current')
sonetLineCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1), )
if mibBuilder.loadTexts: sonetLineCurrentTable.setStatus('current')
sonetLineCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetLineCurrentEntry.setStatus('current')
sonetLineCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineCurrentStatus.setStatus('current')
sonetLineCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineCurrentESs.setStatus('current')
sonetLineCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineCurrentSESs.setStatus('current')
sonetLineCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineCurrentCVs.setStatus('current')
sonetLineCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineCurrentUASs.setStatus('current')
sonetLineIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2), )
if mibBuilder.loadTexts: sonetLineIntervalTable.setStatus('current')
sonetLineIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetLineIntervalNumber"))
if mibBuilder.loadTexts: sonetLineIntervalEntry.setStatus('current')
sonetLineIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetLineIntervalNumber.setStatus('current')
sonetLineIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineIntervalESs.setStatus('current')
sonetLineIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineIntervalSESs.setStatus('current')
sonetLineIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineIntervalCVs.setStatus('current')
sonetLineIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetLineIntervalUASs.setStatus('current')
sonetFarEndLineCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1), )
if mibBuilder.loadTexts: sonetFarEndLineCurrentTable.setStatus('current')
sonetFarEndLineCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetFarEndLineCurrentEntry.setStatus('current')
sonetFarEndLineCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineCurrentESs.setStatus('current')
sonetFarEndLineCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineCurrentSESs.setStatus('current')
sonetFarEndLineCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineCurrentCVs.setStatus('current')
sonetFarEndLineCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineCurrentUASs.setStatus('current')
sonetFarEndLineIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2), )
if mibBuilder.loadTexts: sonetFarEndLineIntervalTable.setStatus('current')
sonetFarEndLineIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndLineIntervalNumber"))
if mibBuilder.loadTexts: sonetFarEndLineIntervalEntry.setStatus('current')
sonetFarEndLineIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetFarEndLineIntervalNumber.setStatus('current')
sonetFarEndLineIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineIntervalESs.setStatus('current')
sonetFarEndLineIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineIntervalSESs.setStatus('current')
sonetFarEndLineIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineIntervalCVs.setStatus('current')
sonetFarEndLineIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndLineIntervalUASs.setStatus('current')
sonetPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1), )
if mibBuilder.loadTexts: sonetPathCurrentTable.setStatus('current')
sonetPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetPathCurrentEntry.setStatus('current')
sonetPathCurrentWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sts1", 1), ("sts3cSTM1", 2), ("sts12cSTM4", 3), ("sts24c", 4), ("sts48cSTM16", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetPathCurrentWidth.setStatus('current')
sonetPathCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathCurrentStatus.setStatus('current')
sonetPathCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathCurrentESs.setStatus('current')
sonetPathCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathCurrentSESs.setStatus('current')
sonetPathCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathCurrentCVs.setStatus('current')
sonetPathCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathCurrentUASs.setStatus('current')
sonetPathIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2), )
if mibBuilder.loadTexts: sonetPathIntervalTable.setStatus('current')
sonetPathIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetPathIntervalNumber"))
if mibBuilder.loadTexts: sonetPathIntervalEntry.setStatus('current')
sonetPathIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetPathIntervalNumber.setStatus('current')
sonetPathIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathIntervalESs.setStatus('current')
sonetPathIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathIntervalSESs.setStatus('current')
sonetPathIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathIntervalCVs.setStatus('current')
sonetPathIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetPathIntervalUASs.setStatus('current')
sonetFarEndPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1), )
if mibBuilder.loadTexts: sonetFarEndPathCurrentTable.setStatus('current')
sonetFarEndPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetFarEndPathCurrentEntry.setStatus('current')
sonetFarEndPathCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathCurrentESs.setStatus('current')
sonetFarEndPathCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathCurrentSESs.setStatus('current')
sonetFarEndPathCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathCurrentCVs.setStatus('current')
sonetFarEndPathCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathCurrentUASs.setStatus('current')
sonetFarEndPathIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2), )
if mibBuilder.loadTexts: sonetFarEndPathIntervalTable.setStatus('current')
sonetFarEndPathIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndPathIntervalNumber"))
if mibBuilder.loadTexts: sonetFarEndPathIntervalEntry.setStatus('current')
sonetFarEndPathIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetFarEndPathIntervalNumber.setStatus('current')
sonetFarEndPathIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathIntervalESs.setStatus('current')
sonetFarEndPathIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathIntervalSESs.setStatus('current')
sonetFarEndPathIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathIntervalCVs.setStatus('current')
sonetFarEndPathIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndPathIntervalUASs.setStatus('current')
sonetVTCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1), )
if mibBuilder.loadTexts: sonetVTCurrentTable.setStatus('current')
sonetVTCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetVTCurrentEntry.setStatus('current')
sonetVTCurrentWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vtWidth15VC11", 1), ("vtWidth2VC12", 2), ("vtWidth3", 3), ("vtWidth6VC2", 4), ("vtWidth6c", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetVTCurrentWidth.setStatus('current')
sonetVTCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTCurrentStatus.setStatus('current')
sonetVTCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTCurrentESs.setStatus('current')
sonetVTCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTCurrentSESs.setStatus('current')
sonetVTCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTCurrentCVs.setStatus('current')
sonetVTCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTCurrentUASs.setStatus('current')
sonetVTIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2), )
if mibBuilder.loadTexts: sonetVTIntervalTable.setStatus('current')
sonetVTIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetVTIntervalNumber"))
if mibBuilder.loadTexts: sonetVTIntervalEntry.setStatus('current')
sonetVTIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetVTIntervalNumber.setStatus('current')
sonetVTIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTIntervalESs.setStatus('current')
sonetVTIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTIntervalSESs.setStatus('current')
sonetVTIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTIntervalCVs.setStatus('current')
sonetVTIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetVTIntervalUASs.setStatus('current')
sonetFarEndVTCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1), )
if mibBuilder.loadTexts: sonetFarEndVTCurrentTable.setStatus('current')
sonetFarEndVTCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sonetFarEndVTCurrentEntry.setStatus('current')
sonetFarEndVTCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTCurrentESs.setStatus('current')
sonetFarEndVTCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTCurrentSESs.setStatus('current')
sonetFarEndVTCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTCurrentCVs.setStatus('current')
sonetFarEndVTCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTCurrentUASs.setStatus('current')
sonetFarEndVTIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2), )
if mibBuilder.loadTexts: sonetFarEndVTIntervalTable.setStatus('current')
sonetFarEndVTIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndVTIntervalNumber"))
if mibBuilder.loadTexts: sonetFarEndVTIntervalEntry.setStatus('current')
sonetFarEndVTIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: sonetFarEndVTIntervalNumber.setStatus('current')
sonetFarEndVTIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTIntervalESs.setStatus('current')
sonetFarEndVTIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTIntervalSESs.setStatus('current')
sonetFarEndVTIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTIntervalCVs.setStatus('current')
sonetFarEndVTIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetFarEndVTIntervalUASs.setStatus('current')
sonetConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4))
sonetGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4, 1))
sonetCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4, 2))
sonetCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 39, 4, 2, 1)).setObjects(("SONET-MIB", "sonetMediumStuff"), ("SONET-MIB", "sonetSectionStuff"), ("SONET-MIB", "sonetLineStuff"), ("SONET-MIB", "sonetFarEndLineStuff"), ("SONET-MIB", "sonetPathStuff"), ("SONET-MIB", "sonetFarEndPathStuff"), ("SONET-MIB", "sonetVTStuff"), ("SONET-MIB", "sonetFarEndVTStuff"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetCompliance = sonetCompliance.setStatus('current')
sonetMediumStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 1)).setObjects(("SONET-MIB", "sonetMediumType"), ("SONET-MIB", "sonetMediumTimeElapsed"), ("SONET-MIB", "sonetMediumValidIntervals"), ("SONET-MIB", "sonetMediumLineCoding"), ("SONET-MIB", "sonetMediumLineType"), ("SONET-MIB", "sonetMediumCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetMediumStuff = sonetMediumStuff.setStatus('current')
sonetSectionStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 2)).setObjects(("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetSectionCurrentESs"), ("SONET-MIB", "sonetSectionCurrentSESs"), ("SONET-MIB", "sonetSectionCurrentSEFSs"), ("SONET-MIB", "sonetSectionCurrentCVs"), ("SONET-MIB", "sonetSectionIntervalESs"), ("SONET-MIB", "sonetSectionIntervalSESs"), ("SONET-MIB", "sonetSectionIntervalSEFSs"), ("SONET-MIB", "sonetSectionIntervalCVs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetSectionStuff = sonetSectionStuff.setStatus('current')
sonetLineStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 3)).setObjects(("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetLineCurrentESs"), ("SONET-MIB", "sonetLineCurrentSESs"), ("SONET-MIB", "sonetLineCurrentCVs"), ("SONET-MIB", "sonetLineCurrentUASs"), ("SONET-MIB", "sonetLineIntervalESs"), ("SONET-MIB", "sonetLineIntervalSESs"), ("SONET-MIB", "sonetLineIntervalCVs"), ("SONET-MIB", "sonetLineIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetLineStuff = sonetLineStuff.setStatus('current')
sonetFarEndLineStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 4)).setObjects(("SONET-MIB", "sonetFarEndLineCurrentESs"), ("SONET-MIB", "sonetFarEndLineCurrentSESs"), ("SONET-MIB", "sonetFarEndLineCurrentCVs"), ("SONET-MIB", "sonetFarEndLineCurrentUASs"), ("SONET-MIB", "sonetFarEndLineIntervalESs"), ("SONET-MIB", "sonetFarEndLineIntervalSESs"), ("SONET-MIB", "sonetFarEndLineIntervalCVs"), ("SONET-MIB", "sonetFarEndLineIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetFarEndLineStuff = sonetFarEndLineStuff.setStatus('current')
sonetPathStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 5)).setObjects(("SONET-MIB", "sonetPathCurrentWidth"), ("SONET-MIB", "sonetPathCurrentStatus"), ("SONET-MIB", "sonetPathCurrentESs"), ("SONET-MIB", "sonetPathCurrentSESs"), ("SONET-MIB", "sonetPathCurrentCVs"), ("SONET-MIB", "sonetPathCurrentUASs"), ("SONET-MIB", "sonetPathIntervalESs"), ("SONET-MIB", "sonetPathIntervalSESs"), ("SONET-MIB", "sonetPathIntervalCVs"), ("SONET-MIB", "sonetPathIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetPathStuff = sonetPathStuff.setStatus('current')
sonetFarEndPathStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 6)).setObjects(("SONET-MIB", "sonetFarEndPathCurrentESs"), ("SONET-MIB", "sonetFarEndPathCurrentSESs"), ("SONET-MIB", "sonetFarEndPathCurrentCVs"), ("SONET-MIB", "sonetFarEndPathCurrentUASs"), ("SONET-MIB", "sonetFarEndPathIntervalESs"), ("SONET-MIB", "sonetFarEndPathIntervalSESs"), ("SONET-MIB", "sonetFarEndPathIntervalCVs"), ("SONET-MIB", "sonetFarEndPathIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetFarEndPathStuff = sonetFarEndPathStuff.setStatus('current')
sonetVTStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 7)).setObjects(("SONET-MIB", "sonetVTCurrentWidth"), ("SONET-MIB", "sonetVTCurrentStatus"), ("SONET-MIB", "sonetVTCurrentESs"), ("SONET-MIB", "sonetVTCurrentSESs"), ("SONET-MIB", "sonetVTCurrentCVs"), ("SONET-MIB", "sonetVTCurrentUASs"), ("SONET-MIB", "sonetVTIntervalESs"), ("SONET-MIB", "sonetVTIntervalSESs"), ("SONET-MIB", "sonetVTIntervalCVs"), ("SONET-MIB", "sonetVTIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetVTStuff = sonetVTStuff.setStatus('current')
sonetFarEndVTStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 8)).setObjects(("SONET-MIB", "sonetFarEndVTCurrentESs"), ("SONET-MIB", "sonetFarEndVTCurrentSESs"), ("SONET-MIB", "sonetFarEndVTCurrentCVs"), ("SONET-MIB", "sonetFarEndVTCurrentUASs"), ("SONET-MIB", "sonetFarEndVTIntervalESs"), ("SONET-MIB", "sonetFarEndVTIntervalSESs"), ("SONET-MIB", "sonetFarEndVTIntervalCVs"), ("SONET-MIB", "sonetFarEndVTIntervalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sonetFarEndVTStuff = sonetFarEndVTStuff.setStatus('current')
mibBuilder.exportSymbols("SONET-MIB", sonetObjectsVT=sonetObjectsVT, sonetSectionIntervalNumber=sonetSectionIntervalNumber, sonetSectionStuff=sonetSectionStuff, sonetSectionCurrentSEFSs=sonetSectionCurrentSEFSs, sonetLineIntervalESs=sonetLineIntervalESs, sonetFarEndLineIntervalNumber=sonetFarEndLineIntervalNumber, sonetFarEndPath=sonetFarEndPath, sonetMediumStuff=sonetMediumStuff, sonetFarEndLineIntervalESs=sonetFarEndLineIntervalESs, sonetFarEndPathCurrentESs=sonetFarEndPathCurrentESs, sonetFarEndVTCurrentSESs=sonetFarEndVTCurrentSESs, sonetFarEndLineCurrentCVs=sonetFarEndLineCurrentCVs, sonetVTIntervalTable=sonetVTIntervalTable, sonetVTCurrentUASs=sonetVTCurrentUASs, sonetFarEndPathStuff=sonetFarEndPathStuff, sonetFarEndLineIntervalTable=sonetFarEndLineIntervalTable, sonetFarEndPathIntervalTable=sonetFarEndPathIntervalTable, sonetFarEndPathCurrentUASs=sonetFarEndPathCurrentUASs, sonetSectionIntervalESs=sonetSectionIntervalESs, sonetSectionIntervalCVs=sonetSectionIntervalCVs, sonetLine=sonetLine, sonetFarEndLineIntervalSESs=sonetFarEndLineIntervalSESs, sonetFarEndVTCurrentESs=sonetFarEndVTCurrentESs, sonetMediumValidIntervals=sonetMediumValidIntervals, sonetLineIntervalEntry=sonetLineIntervalEntry, sonetPathCurrentStatus=sonetPathCurrentStatus, sonetVTStuff=sonetVTStuff, sonetFarEndVTCurrentCVs=sonetFarEndVTCurrentCVs, sonetVTIntervalUASs=sonetVTIntervalUASs, sonetConformance=sonetConformance, sonetLineIntervalTable=sonetLineIntervalTable, sonetLineCurrentEntry=sonetLineCurrentEntry, sonetMediumLineCoding=sonetMediumLineCoding, sonetFarEndPathCurrentTable=sonetFarEndPathCurrentTable, sonetPathCurrentUASs=sonetPathCurrentUASs, sonetSectionIntervalEntry=sonetSectionIntervalEntry, sonetLineCurrentStatus=sonetLineCurrentStatus, sonetPathIntervalNumber=sonetPathIntervalNumber, sonetMedium=sonetMedium, sonetFarEndPathIntervalNumber=sonetFarEndPathIntervalNumber, sonetLineCurrentESs=sonetLineCurrentESs, sonetFarEndPathCurrentSESs=sonetFarEndPathCurrentSESs, sonetSection=sonetSection, sonetPathCurrentESs=sonetPathCurrentESs, sonetFarEndVTIntervalUASs=sonetFarEndVTIntervalUASs, PYSNMP_MODULE_ID=sonetMIB, sonetLineCurrentTable=sonetLineCurrentTable, sonetObjectsPath=sonetObjectsPath, sonetVTIntervalSESs=sonetVTIntervalSESs, sonetFarEndVTIntervalSESs=sonetFarEndVTIntervalSESs, sonetVTCurrentTable=sonetVTCurrentTable, sonetFarEndLine=sonetFarEndLine, sonetMediumCircuitIdentifier=sonetMediumCircuitIdentifier, sonetFarEndVT=sonetFarEndVT, sonetFarEndLineCurrentEntry=sonetFarEndLineCurrentEntry, sonetFarEndVTIntervalCVs=sonetFarEndVTIntervalCVs, sonetCompliance=sonetCompliance, sonetObjects=sonetObjects, sonetFarEndLineStuff=sonetFarEndLineStuff, sonetVTIntervalEntry=sonetVTIntervalEntry, sonetSectionCurrentEntry=sonetSectionCurrentEntry, sonetPathIntervalSESs=sonetPathIntervalSESs, sonetGroups=sonetGroups, sonetFarEndPathIntervalESs=sonetFarEndPathIntervalESs, sonetFarEndLineCurrentTable=sonetFarEndLineCurrentTable, sonetPathStuff=sonetPathStuff, sonetFarEndPathIntervalSESs=sonetFarEndPathIntervalSESs, sonetVTCurrentESs=sonetVTCurrentESs, sonetFarEndVTStuff=sonetFarEndVTStuff, sonetMediumType=sonetMediumType, sonetLineStuff=sonetLineStuff, sonetVTIntervalNumber=sonetVTIntervalNumber, sonetFarEndPathIntervalCVs=sonetFarEndPathIntervalCVs, sonetFarEndVTIntervalEntry=sonetFarEndVTIntervalEntry, sonetFarEndVTCurrentTable=sonetFarEndVTCurrentTable, sonetFarEndPathCurrentEntry=sonetFarEndPathCurrentEntry, sonetFarEndPathIntervalUASs=sonetFarEndPathIntervalUASs, sonetVTCurrentSESs=sonetVTCurrentSESs, sonetVTIntervalCVs=sonetVTIntervalCVs, sonetCompliances=sonetCompliances, sonetMediumTable=sonetMediumTable, sonetSectionIntervalSEFSs=sonetSectionIntervalSEFSs, sonetLineIntervalSESs=sonetLineIntervalSESs, sonetPathCurrentTable=sonetPathCurrentTable, sonetPathCurrentWidth=sonetPathCurrentWidth, sonetFarEndVTCurrentEntry=sonetFarEndVTCurrentEntry, sonetVTCurrentWidth=sonetVTCurrentWidth, sonetSectionCurrentSESs=sonetSectionCurrentSESs, sonetSectionCurrentStatus=sonetSectionCurrentStatus, sonetFarEndLineIntervalUASs=sonetFarEndLineIntervalUASs, sonetFarEndVTIntervalNumber=sonetFarEndVTIntervalNumber, sonetSectionCurrentCVs=sonetSectionCurrentCVs, sonetFarEndVTIntervalESs=sonetFarEndVTIntervalESs, sonetLineCurrentCVs=sonetLineCurrentCVs, sonetFarEndPathCurrentCVs=sonetFarEndPathCurrentCVs, sonetVTCurrentStatus=sonetVTCurrentStatus, sonetLineIntervalUASs=sonetLineIntervalUASs, sonetFarEndLineCurrentESs=sonetFarEndLineCurrentESs, sonetLineCurrentUASs=sonetLineCurrentUASs, sonetFarEndVTCurrentUASs=sonetFarEndVTCurrentUASs, sonetPath=sonetPath, sonetMediumEntry=sonetMediumEntry, sonetPathCurrentCVs=sonetPathCurrentCVs, sonetMediumLineType=sonetMediumLineType, sonetFarEndLineCurrentSESs=sonetFarEndLineCurrentSESs, sonetPathIntervalESs=sonetPathIntervalESs, sonetFarEndVTIntervalTable=sonetFarEndVTIntervalTable, sonetPathIntervalCVs=sonetPathIntervalCVs, sonetFarEndLineCurrentUASs=sonetFarEndLineCurrentUASs, sonetPathIntervalUASs=sonetPathIntervalUASs, sonetVTCurrentCVs=sonetVTCurrentCVs, sonetFarEndLineIntervalEntry=sonetFarEndLineIntervalEntry, sonetSectionIntervalSESs=sonetSectionIntervalSESs, sonetFarEndLineIntervalCVs=sonetFarEndLineIntervalCVs, sonetPathCurrentSESs=sonetPathCurrentSESs, sonetLineCurrentSESs=sonetLineCurrentSESs, sonetVT=sonetVT, sonetMediumTimeElapsed=sonetMediumTimeElapsed, sonetLineIntervalCVs=sonetLineIntervalCVs, sonetPathCurrentEntry=sonetPathCurrentEntry, sonetPathIntervalTable=sonetPathIntervalTable, sonetSectionCurrentESs=sonetSectionCurrentESs, sonetSectionIntervalTable=sonetSectionIntervalTable, sonetMIB=sonetMIB, sonetVTIntervalESs=sonetVTIntervalESs, sonetFarEndPathIntervalEntry=sonetFarEndPathIntervalEntry, sonetLineIntervalNumber=sonetLineIntervalNumber, sonetPathIntervalEntry=sonetPathIntervalEntry, sonetSectionCurrentTable=sonetSectionCurrentTable, sonetVTCurrentEntry=sonetVTCurrentEntry)