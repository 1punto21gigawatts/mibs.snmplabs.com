#
# PySNMP MIB module A3Com-IPSO-r1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-IPSO-R1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, NotificationType, Unsigned32, MibIdentifier, Counter32, Integer32, IpAddress, ModuleIdentity, iso, enterprises, TimeTicks, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Integer32", "IpAddress", "ModuleIdentity", "iso", "enterprises", "TimeTicks", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComIPSO = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 12))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3IPsecureCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 12, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("security1108", 1), ("security1038", 2), ("noSecurity", 3))).clone('noSecurity')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureCtl.setStatus('mandatory')
a3IPsecureFileServer = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 12, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureFileServer.setStatus('mandatory')
a3IPsecureParamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 12, 3), )
if mibBuilder.loadTexts: a3IPsecureParamTable.setStatus('mandatory')
a3IPsecureParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1), ).setIndexNames((0, "A3Com-IPSO-r1-MIB", "a3IPsecureParamPortIndex"))
if mibBuilder.loadTexts: a3IPsecureParamEntry.setStatus('mandatory')
a3IPsecureParamPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsecureParamPortIndex.setStatus('mandatory')
a3IPsecureParamCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureParamCtl.setStatus('mandatory')
a3IPsecureLabelDefaultLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("topSecret", 2), ("secret", 3), ("confidential", 4), ("unclassified", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureLabelDefaultLevel.setStatus('mandatory')
a3IPsecureLabelDefaultAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureLabelDefaultAuth.setStatus('mandatory')
a3IPsecureLabelSysLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("topSecret", 2), ("secret", 3), ("confidential", 4), ("unclassified", 5))).clone('unclassified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureLabelSysLevel.setStatus('mandatory')
a3IPsecureLabelSysAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 6), Integer32().clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureLabelSysAuth.setStatus('mandatory')
a3IPsecureMinLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("topSecret", 1), ("secret", 2), ("confidential", 3), ("unclassified", 4))).clone('unclassified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureMinLevel.setStatus('mandatory')
a3IPsecureMaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("topSecret", 1), ("secret", 2), ("confidential", 3), ("unclassified", 4))).clone('unclassified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureMaxLevel.setStatus('mandatory')
a3IPsecureAuthInTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 12, 4), )
if mibBuilder.loadTexts: a3IPsecureAuthInTable.setStatus('mandatory')
a3IPsecureAuthInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1), ).setIndexNames((0, "A3Com-IPSO-r1-MIB", "a3IPsecureAuthInPort"), (0, "A3Com-IPSO-r1-MIB", "a3IPsecureAuthInFlags"))
if mibBuilder.loadTexts: a3IPsecureAuthInEntry.setStatus('mandatory')
a3IPsecureAuthInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsecureAuthInPort.setStatus('mandatory')
a3IPsecureAuthInFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsecureAuthInFlags.setStatus('mandatory')
a3IPsecureAuthInMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("any", 2))).clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureAuthInMatch.setStatus('mandatory')
a3IPsecureAuthInStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureAuthInStatus.setStatus('mandatory')
a3IPsecureAuthOutTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 12, 5), )
if mibBuilder.loadTexts: a3IPsecureAuthOutTable.setStatus('mandatory')
a3IPsecureAuthOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1), ).setIndexNames((0, "A3Com-IPSO-r1-MIB", "a3IPsecureAuthOutPort"), (0, "A3Com-IPSO-r1-MIB", "a3IPsecureAuthOutFlags"))
if mibBuilder.loadTexts: a3IPsecureAuthOutEntry.setStatus('mandatory')
a3IPsecureAuthOutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsecureAuthOutPort.setStatus('mandatory')
a3IPsecureAuthOutFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsecureAuthOutFlags.setStatus('mandatory')
a3IPsecureAuthOutMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("any", 2))).clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureAuthOutMatch.setStatus('mandatory')
a3IPsecureAuthOutStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsecureAuthOutStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3Com-IPSO-r1-MIB", a3IPsecureParamCtl=a3IPsecureParamCtl, a3IPsecureParamPortIndex=a3IPsecureParamPortIndex, a3IPsecureAuthInTable=a3IPsecureAuthInTable, a3IPsecureAuthInPort=a3IPsecureAuthInPort, a3IPsecureLabelDefaultAuth=a3IPsecureLabelDefaultAuth, a3IPsecureAuthInStatus=a3IPsecureAuthInStatus, RowStatus=RowStatus, a3IPsecureParamEntry=a3IPsecureParamEntry, brouterMIB=brouterMIB, a3IPsecureLabelDefaultLevel=a3IPsecureLabelDefaultLevel, a3Com=a3Com, a3IPsecureAuthOutStatus=a3IPsecureAuthOutStatus, a3IPsecureAuthOutTable=a3IPsecureAuthOutTable, a3IPsecureMinLevel=a3IPsecureMinLevel, a3IPsecureAuthInMatch=a3IPsecureAuthInMatch, a3IPsecureLabelSysAuth=a3IPsecureLabelSysAuth, a3IPsecureCtl=a3IPsecureCtl, a3IPsecureAuthInEntry=a3IPsecureAuthInEntry, a3IPsecureMaxLevel=a3IPsecureMaxLevel, a3IPsecureFileServer=a3IPsecureFileServer, a3IPsecureAuthInFlags=a3IPsecureAuthInFlags, a3IPsecureLabelSysLevel=a3IPsecureLabelSysLevel, a3IPsecureAuthOutPort=a3IPsecureAuthOutPort, a3ComIPSO=a3ComIPSO, a3IPsecureAuthOutEntry=a3IPsecureAuthOutEntry, a3IPsecureAuthOutFlags=a3IPsecureAuthOutFlags, a3IPsecureAuthOutMatch=a3IPsecureAuthOutMatch, a3IPsecureParamTable=a3IPsecureParamTable)
