#
# PySNMP MIB module ORAINTERCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ORAINTERCHANGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Counter64, NotificationType, Integer32, Unsigned32, IpAddress, MibIdentifier, enterprises, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Counter64", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibIdentifier", "enterprises", "Bits", "ModuleIdentity")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
oracle = MibIdentifier((1, 3, 6, 1, 4, 1, 111))
oraInterchangeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 7))
oraInterchangeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 7, 1))
oraInterchgTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 1), )
if mibBuilder.loadTexts: oraInterchgTable.setStatus('mandatory')
oraInterchgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraInterchgEntry.setStatus('mandatory')
oraInterchgConfigDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraInterchgConfigDirectory.setStatus('mandatory')
oraInterchgContactInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraInterchgContactInfo.setStatus('mandatory')
oraNavigatorTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 2), )
if mibBuilder.loadTexts: oraNavigatorTable.setStatus('mandatory')
oraNavigatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraNavigatorEntry.setStatus('mandatory')
oraNavigatorRunningTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorRunningTime.setStatus('mandatory')
oraNavigatorLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNavigatorLogging.setStatus('mandatory')
oraNavigatorLoggingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all", 1), ("errors", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNavigatorLoggingLevel.setStatus('mandatory')
oraNavigatorLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorLogFile.setStatus('mandatory')
oraNavigatorTraceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2), ("level3", 3), ("user", 4), ("level5", 5), ("admin", 6), ("level7", 7), ("level8", 8), ("level9", 9), ("level10", 10), ("level11", 11), ("level12", 12), ("level13", 13), ("level14", 14), ("level15", 15), ("level16", 16), ("off", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNavigatorTraceLevel.setStatus('mandatory')
oraNavigatorTraceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorTraceFile.setStatus('mandatory')
oraNavigatorStoppable = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNavigatorStoppable.setStatus('mandatory')
oraNavigatorAccumulatedSuccessfulRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorAccumulatedSuccessfulRequests.setStatus('mandatory')
oraNavigatorAccumulatedFailedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorAccumulatedFailedRequests.setStatus('mandatory')
oraNavigatorState = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorState.setStatus('mandatory')
oraNavigatorErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorErrors.setStatus('mandatory')
oraNavigatorErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorErrorMessage.setStatus('mandatory')
oraNavigatorListenAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 3), )
if mibBuilder.loadTexts: oraNavigatorListenAddressTable.setStatus('mandatory')
oraNavigatorListenAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraNavigatorListenAddressIndex"))
if mibBuilder.loadTexts: oraNavigatorListenAddressEntry.setStatus('mandatory')
oraNavigatorListenAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorListenAddressIndex.setStatus('mandatory')
oraNavigatorListenAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorListenAddress.setStatus('mandatory')
oraNavigatorFailedAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 4), )
if mibBuilder.loadTexts: oraNavigatorFailedAddressTable.setStatus('mandatory')
oraNavigatorFailedAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraNavigatorFailedAddressIndex"))
if mibBuilder.loadTexts: oraNavigatorFailedAddressEntry.setStatus('mandatory')
oraNavigatorFailedAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorFailedAddressIndex.setStatus('mandatory')
oraNavigatorFailedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorFailedAddress.setStatus('mandatory')
oraNavigatorRouteAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 5), )
if mibBuilder.loadTexts: oraNavigatorRouteAddressTable.setStatus('mandatory')
oraNavigatorRouteAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraNavigatorRouteAddressIndex"))
if mibBuilder.loadTexts: oraNavigatorRouteAddressEntry.setStatus('mandatory')
oraNavigatorRouteAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorRouteAddressIndex.setStatus('mandatory')
oraNavigatorRouteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNavigatorRouteAddress.setStatus('mandatory')
oraCmanagerTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 6), )
if mibBuilder.loadTexts: oraCmanagerTable.setStatus('mandatory')
oraCmanagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraCmanagerEntry.setStatus('mandatory')
oraCmanagerStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerStartTime.setStatus('mandatory')
oraCmanagerRunningTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerRunningTime.setStatus('mandatory')
oraCmanagerLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerLogging.setStatus('mandatory')
oraCmanagerLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerLogFile.setStatus('mandatory')
oraCmanagerTraceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2), ("level3", 3), ("user", 4), ("level5", 5), ("admin", 6), ("level7", 7), ("level8", 8), ("level9", 9), ("level10", 10), ("level11", 11), ("level12", 12), ("level13", 13), ("level14", 14), ("level15", 15), ("level16", 16), ("off", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerTraceLevel.setStatus('mandatory')
oraCmanagerTraceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerTraceFile.setStatus('mandatory')
oraCmanagerStoppable = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerStoppable.setStatus('mandatory')
oraCmanagerMaximumPumps = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerMaximumPumps.setStatus('mandatory')
oraCmanagerMaximumConnectionsPerPump = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerMaximumConnectionsPerPump.setStatus('mandatory')
oraCmanagerPumpStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("distribute", 1), ("group", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraCmanagerPumpStrategy.setStatus('mandatory')
oraCmanagerActivePumps = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerActivePumps.setStatus('mandatory')
oraCmanagerMaximumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerMaximumConnections.setStatus('mandatory')
oraCmanagerCurrentConnectionsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerCurrentConnectionsInUse.setStatus('mandatory')
oraCmanagerAccumulatedSuccessfulConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerAccumulatedSuccessfulConnections.setStatus('mandatory')
oraCmanagerAccumulatedFailedConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerAccumulatedFailedConnections.setStatus('mandatory')
oraCmanagerImmediateAverageBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerImmediateAverageBytes.setStatus('mandatory')
oraCmanagerMaximumConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerMaximumConnectTime.setStatus('mandatory')
oraCmanagerMinimumConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerMinimumConnectTime.setStatus('mandatory')
oraCmanagerAverageConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerAverageConnectTime.setStatus('mandatory')
oraCmanagerMaximumConnectDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerMaximumConnectDuration.setStatus('mandatory')
oraCmanagerState = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerState.setStatus('mandatory')
oraCmanagerErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerErrors.setStatus('mandatory')
oraCmanagerErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerErrorMessage.setStatus('mandatory')
oraCmanagerListenAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 7), )
if mibBuilder.loadTexts: oraCmanagerListenAddressTable.setStatus('mandatory')
oraCmanagerListenAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraCmanagerListenAddressIndex"))
if mibBuilder.loadTexts: oraCmanagerListenAddressEntry.setStatus('mandatory')
oraCmanagerListenAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerListenAddressIndex.setStatus('mandatory')
oraCmanagerListenAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerListenAddress.setStatus('mandatory')
oraCmanagerFailedAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 8), )
if mibBuilder.loadTexts: oraCmanagerFailedAddressTable.setStatus('mandatory')
oraCmanagerFailedAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraCmanagerFailedAddressIndex"))
if mibBuilder.loadTexts: oraCmanagerFailedAddressEntry.setStatus('mandatory')
oraCmanagerFailedAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerFailedAddressIndex.setStatus('mandatory')
oraCmanagerFailedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraCmanagerFailedAddress.setStatus('mandatory')
oraPumpTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 9), )
if mibBuilder.loadTexts: oraPumpTable.setStatus('mandatory')
oraPumpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"))
if mibBuilder.loadTexts: oraPumpEntry.setStatus('mandatory')
oraPumpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpIndex.setStatus('mandatory')
oraPumpActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpActiveTime.setStatus('mandatory')
oraPumpTraceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2), ("level3", 3), ("user", 4), ("level5", 5), ("admin", 6), ("level7", 7), ("level8", 8), ("level9", 9), ("level10", 10), ("level11", 11), ("level12", 12), ("level13", 13), ("level14", 14), ("level15", 15), ("level16", 16), ("off", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraPumpTraceLevel.setStatus('mandatory')
oraPumpTraceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpTraceFile.setStatus('mandatory')
oraPumpActiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpActiveConnections.setStatus('mandatory')
oraPumpSuccessfulConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpSuccessfulConnections.setStatus('mandatory')
oraPumpFailedConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpFailedConnections.setStatus('mandatory')
oraPumpAccumulatedBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpAccumulatedBytesSent.setStatus('mandatory')
oraPumpCurrentBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpCurrentBytesPerSecond.setStatus('mandatory')
oraPumpMaximumAverageBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpMaximumAverageBytes.setStatus('mandatory')
oraPumpImmediateAverageBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpImmediateAverageBytes.setStatus('mandatory')
oraPumpMaximumConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpMaximumConnectTime.setStatus('mandatory')
oraPumpMinimumConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpMinimumConnectTime.setStatus('mandatory')
oraPumpAverageConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpAverageConnectTime.setStatus('mandatory')
oraPumpMaximumConnectDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpMaximumConnectDuration.setStatus('mandatory')
oraPumpMaximumBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraPumpMaximumBuffers.setStatus('mandatory')
oraPumpBufferUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpBufferUtilization.setStatus('mandatory')
oraPumpErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpErrors.setStatus('mandatory')
oraPumpErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpErrorMessage.setStatus('mandatory')
oraPumpListenAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 10), )
if mibBuilder.loadTexts: oraPumpListenAddressTable.setStatus('mandatory')
oraPumpListenAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpListenAddressIndex"))
if mibBuilder.loadTexts: oraPumpListenAddressEntry.setStatus('mandatory')
oraPumpListenAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpListenAddressIndex.setStatus('mandatory')
oraPumpListenAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpListenAddress.setStatus('mandatory')
oraPumpFailedAddressTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 11), )
if mibBuilder.loadTexts: oraPumpFailedAddressTable.setStatus('mandatory')
oraPumpFailedAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpFailedAddressIndex"))
if mibBuilder.loadTexts: oraPumpFailedAddressEntry.setStatus('mandatory')
oraPumpFailedAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpFailedAddressIndex.setStatus('mandatory')
oraPumpFailedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraPumpFailedAddress.setStatus('mandatory')
oraConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 111, 7, 1, 12), )
if mibBuilder.loadTexts: oraConnectionTable.setStatus('mandatory')
oraConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"), (0, "ORAINTERCHANGE-MIB", "oraConnectionIndex"))
if mibBuilder.loadTexts: oraConnectionEntry.setStatus('mandatory')
oraConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraConnectionIndex.setStatus('mandatory')
oraConnectionPumpID = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraConnectionPumpID.setStatus('mandatory')
oraConnectionIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraConnectionIdleTime.setStatus('mandatory')
oraConnectionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraConnectionDuration.setStatus('mandatory')
oraConnectionSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraConnectionSourceAddress.setStatus('mandatory')
oraConnectionDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraConnectionDestinationAddress.setStatus('mandatory')
oraInterchgTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 7, 2))
oraNavigatorStateChange = NotificationType((1, 3, 6, 1, 4, 1, 111, 7, 2) + (0,1)).setObjects(("ORAINTERCHANGE-MIB", "oraNavigatorState"))
oraCmanagerStateChange = NotificationType((1, 3, 6, 1, 4, 1, 111, 7, 2) + (0,2)).setObjects(("ORAINTERCHANGE-MIB", "oraCmanagerState"))
mibBuilder.exportSymbols("ORAINTERCHANGE-MIB", oraNavigatorRouteAddressTable=oraNavigatorRouteAddressTable, oraCmanagerAccumulatedSuccessfulConnections=oraCmanagerAccumulatedSuccessfulConnections, oraCmanagerErrorMessage=oraCmanagerErrorMessage, oraNavigatorLogFile=oraNavigatorLogFile, oraNavigatorFailedAddressTable=oraNavigatorFailedAddressTable, oraNavigatorTraceLevel=oraNavigatorTraceLevel, oraCmanagerListenAddressTable=oraCmanagerListenAddressTable, oraNavigatorRouteAddressIndex=oraNavigatorRouteAddressIndex, oraNavigatorListenAddressTable=oraNavigatorListenAddressTable, oraPumpMaximumBuffers=oraPumpMaximumBuffers, oraConnectionSourceAddress=oraConnectionSourceAddress, oraNavigatorRunningTime=oraNavigatorRunningTime, oraCmanagerFailedAddressEntry=oraCmanagerFailedAddressEntry, oraPumpSuccessfulConnections=oraPumpSuccessfulConnections, oraCmanagerAccumulatedFailedConnections=oraCmanagerAccumulatedFailedConnections, oraNavigatorErrors=oraNavigatorErrors, oraNavigatorLoggingLevel=oraNavigatorLoggingLevel, oraPumpTraceLevel=oraPumpTraceLevel, oraInterchgTable=oraInterchgTable, oraNavigatorTraceFile=oraNavigatorTraceFile, oraInterchangeMIB=oraInterchangeMIB, oraPumpFailedAddress=oraPumpFailedAddress, oraCmanagerFailedAddressIndex=oraCmanagerFailedAddressIndex, oraPumpTable=oraPumpTable, oraCmanagerListenAddressIndex=oraCmanagerListenAddressIndex, oraConnectionIndex=oraConnectionIndex, oraConnectionIdleTime=oraConnectionIdleTime, oraCmanagerImmediateAverageBytes=oraCmanagerImmediateAverageBytes, oraCmanagerEntry=oraCmanagerEntry, oraCmanagerFailedAddress=oraCmanagerFailedAddress, oraCmanagerLogFile=oraCmanagerLogFile, oraPumpActiveTime=oraPumpActiveTime, oraPumpAverageConnectTime=oraPumpAverageConnectTime, oraPumpMaximumConnectDuration=oraPumpMaximumConnectDuration, oraPumpTraceFile=oraPumpTraceFile, oraNavigatorState=oraNavigatorState, oraPumpFailedAddressEntry=oraPumpFailedAddressEntry, oraNavigatorAccumulatedFailedRequests=oraNavigatorAccumulatedFailedRequests, oraPumpIndex=oraPumpIndex, oraNavigatorRouteAddress=oraNavigatorRouteAddress, oraPumpActiveConnections=oraPumpActiveConnections, oraCmanagerRunningTime=oraCmanagerRunningTime, oraPumpMinimumConnectTime=oraPumpMinimumConnectTime, oraPumpListenAddressTable=oraPumpListenAddressTable, oraCmanagerAverageConnectTime=oraCmanagerAverageConnectTime, oraPumpImmediateAverageBytes=oraPumpImmediateAverageBytes, oraCmanagerMinimumConnectTime=oraCmanagerMinimumConnectTime, oracle=oracle, oraPumpAccumulatedBytesSent=oraPumpAccumulatedBytesSent, oraConnectionDestinationAddress=oraConnectionDestinationAddress, oraConnectionEntry=oraConnectionEntry, oraNavigatorErrorMessage=oraNavigatorErrorMessage, oraCmanagerTraceFile=oraCmanagerTraceFile, oraConnectionTable=oraConnectionTable, oraCmanagerStateChange=oraCmanagerStateChange, oraInterchgContactInfo=oraInterchgContactInfo, oraCmanagerLogging=oraCmanagerLogging, oraNavigatorStateChange=oraNavigatorStateChange, oraNavigatorListenAddressIndex=oraNavigatorListenAddressIndex, oraPumpListenAddressEntry=oraPumpListenAddressEntry, oraCmanagerStartTime=oraCmanagerStartTime, oraCmanagerListenAddress=oraCmanagerListenAddress, oraNavigatorStoppable=oraNavigatorStoppable, oraCmanagerState=oraCmanagerState, oraPumpBufferUtilization=oraPumpBufferUtilization, oraNavigatorFailedAddressEntry=oraNavigatorFailedAddressEntry, oraInterchgTraps=oraInterchgTraps, oraPumpFailedAddressIndex=oraPumpFailedAddressIndex, oraCmanagerListenAddressEntry=oraCmanagerListenAddressEntry, oraPumpEntry=oraPumpEntry, oraNavigatorLogging=oraNavigatorLogging, oraCmanagerMaximumConnectTime=oraCmanagerMaximumConnectTime, oraCmanagerTable=oraCmanagerTable, oraInterchangeObjects=oraInterchangeObjects, oraPumpFailedConnections=oraPumpFailedConnections, oraPumpErrors=oraPumpErrors, oraCmanagerCurrentConnectionsInUse=oraCmanagerCurrentConnectionsInUse, oraCmanagerMaximumConnections=oraCmanagerMaximumConnections, oraNavigatorListenAddressEntry=oraNavigatorListenAddressEntry, oraNavigatorEntry=oraNavigatorEntry, oraInterchgConfigDirectory=oraInterchgConfigDirectory, oraNavigatorFailedAddress=oraNavigatorFailedAddress, oraPumpListenAddressIndex=oraPumpListenAddressIndex, oraPumpListenAddress=oraPumpListenAddress, oraPumpFailedAddressTable=oraPumpFailedAddressTable, oraCmanagerStoppable=oraCmanagerStoppable, oraCmanagerMaximumConnectDuration=oraCmanagerMaximumConnectDuration, oraPumpMaximumConnectTime=oraPumpMaximumConnectTime, oraNavigatorListenAddress=oraNavigatorListenAddress, oraConnectionPumpID=oraConnectionPumpID, oraConnectionDuration=oraConnectionDuration, oraNavigatorRouteAddressEntry=oraNavigatorRouteAddressEntry, oraCmanagerActivePumps=oraCmanagerActivePumps, oraCmanagerMaximumPumps=oraCmanagerMaximumPumps, oraCmanagerFailedAddressTable=oraCmanagerFailedAddressTable, oraPumpCurrentBytesPerSecond=oraPumpCurrentBytesPerSecond, oraCmanagerTraceLevel=oraCmanagerTraceLevel, oraInterchgEntry=oraInterchgEntry, oraCmanagerPumpStrategy=oraCmanagerPumpStrategy, oraPumpMaximumAverageBytes=oraPumpMaximumAverageBytes, oraNavigatorAccumulatedSuccessfulRequests=oraNavigatorAccumulatedSuccessfulRequests, oraNavigatorFailedAddressIndex=oraNavigatorFailedAddressIndex, oraNavigatorTable=oraNavigatorTable, oraCmanagerMaximumConnectionsPerPump=oraCmanagerMaximumConnectionsPerPump, oraCmanagerErrors=oraCmanagerErrors, oraPumpErrorMessage=oraPumpErrorMessage)