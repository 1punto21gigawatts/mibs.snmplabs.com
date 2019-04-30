#
# PySNMP MIB module XEDIA-DRIVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-DRIVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, IpAddress, iso, TimeTicks, Bits, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "iso", "TimeTicks", "Bits", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaDriverMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 6))
if mibBuilder.loadTexts: xediaDriverMIB.setLastUpdated('9703252155Z')
if mibBuilder.loadTexts: xediaDriverMIB.setOrganization('Xedia Corp.')
xdriverObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 6, 1))
xdriverConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 6, 2))
xdriverStatsTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1), )
if mibBuilder.loadTexts: xdriverStatsTable.setStatus('current')
xdriverStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xdriverStatsEntry.setStatus('current')
xdriverStatsInternalQOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInternalQOverflows.setStatus('current')
xdriverStatsOutGoodFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsOutGoodFrames.setStatus('current')
xdriverStatsOutPercentGood = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsOutPercentGood.setStatus('current')
xdriverStatsOutPercentBad = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsOutPercentBad.setStatus('current')
xdriverStatsOutAvgFrameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsOutAvgFrameLen.setStatus('current')
xdriverStatsInCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInCRCErrors.setStatus('current')
xdriverStatsInGoodFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInGoodFrames.setStatus('current')
xdriverStatsInNoResources = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInNoResources.setStatus('current')
xdriverStatsInPercentGood = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInPercentGood.setStatus('current')
xdriverStatsInPercentBad = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInPercentBad.setStatus('current')
xdriverStatsInAvgFrameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 6, 1, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdriverStatsInAvgFrameLen.setStatus('current')
xdriverCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 1))
xdriverGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 2))
xdriverCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 1, 1)).setObjects(("XEDIA-DRIVER-MIB", "xdriverGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xdriverCompliance = xdriverCompliance.setStatus('current')
xdriverGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 6, 2, 2, 1)).setObjects(("XEDIA-DRIVER-MIB", "xdriverStatsInternalQOverflows"), ("XEDIA-DRIVER-MIB", "xdriverStatsOutGoodFrames"), ("XEDIA-DRIVER-MIB", "xdriverStatsOutPercentGood"), ("XEDIA-DRIVER-MIB", "xdriverStatsOutPercentBad"), ("XEDIA-DRIVER-MIB", "xdriverStatsOutAvgFrameLen"), ("XEDIA-DRIVER-MIB", "xdriverStatsInCRCErrors"), ("XEDIA-DRIVER-MIB", "xdriverStatsInGoodFrames"), ("XEDIA-DRIVER-MIB", "xdriverStatsInNoResources"), ("XEDIA-DRIVER-MIB", "xdriverStatsInPercentGood"), ("XEDIA-DRIVER-MIB", "xdriverStatsInPercentBad"), ("XEDIA-DRIVER-MIB", "xdriverStatsInAvgFrameLen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xdriverGroup = xdriverGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-DRIVER-MIB", xdriverStatsOutGoodFrames=xdriverStatsOutGoodFrames, xdriverStatsEntry=xdriverStatsEntry, xdriverCompliances=xdriverCompliances, xdriverStatsInPercentBad=xdriverStatsInPercentBad, xdriverStatsInternalQOverflows=xdriverStatsInternalQOverflows, xdriverStatsInNoResources=xdriverStatsInNoResources, xdriverConformance=xdriverConformance, xdriverGroups=xdriverGroups, xdriverObjects=xdriverObjects, xdriverCompliance=xdriverCompliance, xdriverStatsOutPercentGood=xdriverStatsOutPercentGood, xdriverStatsInCRCErrors=xdriverStatsInCRCErrors, xdriverGroup=xdriverGroup, xdriverStatsInGoodFrames=xdriverStatsInGoodFrames, PYSNMP_MODULE_ID=xediaDriverMIB, xdriverStatsInPercentGood=xdriverStatsInPercentGood, xediaDriverMIB=xediaDriverMIB, xdriverStatsInAvgFrameLen=xdriverStatsInAvgFrameLen, xdriverStatsTable=xdriverStatsTable, xdriverStatsOutPercentBad=xdriverStatsOutPercentBad, xdriverStatsOutAvgFrameLen=xdriverStatsOutAvgFrameLen)