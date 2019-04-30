#
# PySNMP MIB module HP-ICF-LINKTEST (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-LINKTEST
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hpicfCommon, hpicfObjectModules = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon", "hpicfObjectModules")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, NotificationType, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, ObjectIdentity, Counter64, IpAddress, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Counter64", "IpAddress", "Counter32", "TimeTicks")
TextualConvention, DisplayString, RowStatus, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TimeInterval")
hpicfLinkTestMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7))
hpicfLinkTestMib.setRevisions(('2000-11-03 22:25', '1997-03-06 03:38', '1996-09-06 22:18',))
if mibBuilder.loadTexts: hpicfLinkTestMib.setLastUpdated('200011032225Z')
if mibBuilder.loadTexts: hpicfLinkTestMib.setOrganization('HP Networking')
hpicfLinktest = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6))
hpicfLinkTestNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLinkTestNextIndex.setStatus('current')
hpicfLinkTestTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2), )
if mibBuilder.loadTexts: hpicfLinkTestTable.setStatus('current')
hpicfLinkTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1), ).setIndexNames((0, "HP-ICF-LINKTEST", "hpicfLinkTestIndex"))
if mibBuilder.loadTexts: hpicfLinkTestEntry.setStatus('current')
hpicfLinkTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfLinkTestIndex.setStatus('current')
hpicfLinkTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("icmpEcho", 1), ("ieee8022Test", 2), ("ipxDiagnostic", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestType.setStatus('current')
hpicfLinkTestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(6, 6), ValueSizeConstraint(10, 10), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestAddress.setStatus('current')
hpicfLinkTestIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestIfIndex.setStatus('current')
hpicfLinkTestTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 5), TimeInterval().clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestTimeout.setStatus('current')
hpicfLinkTestRepetitions = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestRepetitions.setStatus('current')
hpicfLinkTestAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLinkTestAttempts.setStatus('current')
hpicfLinkTestSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLinkTestSuccesses.setStatus('current')
hpicfLinkTestMinRespTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLinkTestMinRespTime.setStatus('current')
hpicfLinkTestMaxRespTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLinkTestMaxRespTime.setStatus('current')
hpicfLinkTestTotalRespTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLinkTestTotalRespTime.setStatus('current')
hpicfLinkTestOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 12), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestOwner.setStatus('current')
hpicfLinkTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestStatus.setStatus('current')
hpicfLinkTestDeleteMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keepWhenDone", 1), ("destroyWhenDone", 2))).clone('keepWhenDone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLinkTestDeleteMode.setStatus('current')
hpicfLinkTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1))
hpicfLinkTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1))
hpicfLinkTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2))
hpicfLinkTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1, 1)).setObjects(("HP-ICF-LINKTEST", "hpicfLinkTestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLinkTestCompliance = hpicfLinkTestCompliance.setStatus('deprecated')
hpicfLinkTestCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 1, 2)).setObjects(("HP-ICF-LINKTEST", "hpicfLinkTestGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLinkTestCompliance2 = hpicfLinkTestCompliance2.setStatus('current')
hpicfLinkTestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2, 1)).setObjects(("HP-ICF-LINKTEST", "hpicfLinkTestNextIndex"), ("HP-ICF-LINKTEST", "hpicfLinkTestType"), ("HP-ICF-LINKTEST", "hpicfLinkTestAddress"), ("HP-ICF-LINKTEST", "hpicfLinkTestIfIndex"), ("HP-ICF-LINKTEST", "hpicfLinkTestTimeout"), ("HP-ICF-LINKTEST", "hpicfLinkTestRepetitions"), ("HP-ICF-LINKTEST", "hpicfLinkTestAttempts"), ("HP-ICF-LINKTEST", "hpicfLinkTestSuccesses"), ("HP-ICF-LINKTEST", "hpicfLinkTestMinRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestMaxRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestTotalRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestOwner"), ("HP-ICF-LINKTEST", "hpicfLinkTestStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLinkTestGroup = hpicfLinkTestGroup.setStatus('deprecated')
hpicfLinkTestGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7, 1, 2, 2)).setObjects(("HP-ICF-LINKTEST", "hpicfLinkTestNextIndex"), ("HP-ICF-LINKTEST", "hpicfLinkTestType"), ("HP-ICF-LINKTEST", "hpicfLinkTestAddress"), ("HP-ICF-LINKTEST", "hpicfLinkTestIfIndex"), ("HP-ICF-LINKTEST", "hpicfLinkTestTimeout"), ("HP-ICF-LINKTEST", "hpicfLinkTestRepetitions"), ("HP-ICF-LINKTEST", "hpicfLinkTestAttempts"), ("HP-ICF-LINKTEST", "hpicfLinkTestSuccesses"), ("HP-ICF-LINKTEST", "hpicfLinkTestMinRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestMaxRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestTotalRespTime"), ("HP-ICF-LINKTEST", "hpicfLinkTestOwner"), ("HP-ICF-LINKTEST", "hpicfLinkTestStatus"), ("HP-ICF-LINKTEST", "hpicfLinkTestDeleteMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLinkTestGroup2 = hpicfLinkTestGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-LINKTEST", hpicfLinkTestTable=hpicfLinkTestTable, hpicfLinkTestMinRespTime=hpicfLinkTestMinRespTime, hpicfLinkTestDeleteMode=hpicfLinkTestDeleteMode, hpicfLinkTestIndex=hpicfLinkTestIndex, hpicfLinkTestRepetitions=hpicfLinkTestRepetitions, hpicfLinkTestType=hpicfLinkTestType, hpicfLinkTestConformance=hpicfLinkTestConformance, hpicfLinkTestIfIndex=hpicfLinkTestIfIndex, hpicfLinkTestTimeout=hpicfLinkTestTimeout, hpicfLinkTestGroup=hpicfLinkTestGroup, hpicfLinkTestCompliance=hpicfLinkTestCompliance, hpicfLinkTestSuccesses=hpicfLinkTestSuccesses, hpicfLinktest=hpicfLinktest, hpicfLinkTestGroups=hpicfLinkTestGroups, hpicfLinkTestMaxRespTime=hpicfLinkTestMaxRespTime, hpicfLinkTestNextIndex=hpicfLinkTestNextIndex, hpicfLinkTestCompliances=hpicfLinkTestCompliances, hpicfLinkTestGroup2=hpicfLinkTestGroup2, hpicfLinkTestOwner=hpicfLinkTestOwner, hpicfLinkTestStatus=hpicfLinkTestStatus, hpicfLinkTestEntry=hpicfLinkTestEntry, hpicfLinkTestTotalRespTime=hpicfLinkTestTotalRespTime, hpicfLinkTestAttempts=hpicfLinkTestAttempts, PYSNMP_MODULE_ID=hpicfLinkTestMib, hpicfLinkTestAddress=hpicfLinkTestAddress, hpicfLinkTestCompliance2=hpicfLinkTestCompliance2, hpicfLinkTestMib=hpicfLinkTestMib)