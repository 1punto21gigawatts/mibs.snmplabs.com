#
# PySNMP MIB module HPN-ICF-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-T1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, TimeTicks, Unsigned32, Counter64, NotificationType, Gauge32, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfT1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29))
hpnicfT1.setRevisions(('2012-07-16 17:41', '2009-06-08 17:41', '2004-12-01 14:36',))
if mibBuilder.loadTexts: hpnicfT1.setLastUpdated('201207161741Z')
if mibBuilder.loadTexts: hpnicfT1.setOrganization('')
hpnicft1InterfaceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1), )
if mibBuilder.loadTexts: hpnicft1InterfaceStatusTable.setStatus('current')
hpnicft1InterfaceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicft1InterfaceStatusEntry.setStatus('current')
hpnicft1InterfaceInErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInErrs.setStatus('current')
hpnicft1InterfaceInRuntsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInRuntsErrs.setStatus('current')
hpnicft1InterfaceInGiantsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInGiantsErrs.setStatus('current')
hpnicft1InterfaceInCrcErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInCrcErrs.setStatus('current')
hpnicft1InterfaceInAlignErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInAlignErrs.setStatus('current')
hpnicft1InterfaceInOverRunsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInOverRunsErrs.setStatus('current')
hpnicft1InterfaceInDribblesErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInDribblesErrs.setStatus('current')
hpnicft1InterfaceInAbortedSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInAbortedSeqErrs.setStatus('current')
hpnicft1InterfaceInNoBufferErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInNoBufferErrs.setStatus('current')
hpnicft1InterfaceInFramingErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceInFramingErrs.setStatus('current')
hpnicft1InterfaceOutputErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceOutputErrs.setStatus('current')
hpnicft1InterfaceOutUnderRunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceOutUnderRunErrs.setStatus('current')
hpnicft1InterfaceOutCollisonsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceOutCollisonsErrs.setStatus('current')
hpnicft1InterfaceOutDeferedErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1InterfaceOutDeferedErrs.setStatus('current')
hpnicft1Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2), )
if mibBuilder.loadTexts: hpnicft1Table.setStatus('current')
hpnicft1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicft1Entry.setStatus('current')
class HpnicfT1TimeSlot(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

hpnicft1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 1), Bits().clone(namedValues=NamedValues(("voice", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1Type.setStatus('current')
hpnicft1Clock = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("slave", 1), ("master", 2), ("internal", 3), ("line", 4), ("linePri", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicft1Clock.setStatus('current')
hpnicft1FrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sf", 1), ("esf", 2))).clone('esf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicft1FrameFormat.setStatus('current')
hpnicft1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ami", 1), ("b8zs", 2))).clone('b8zs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicft1LineCode.setStatus('current')
hpnicft1PriSetTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 5), HpnicfT1TimeSlot()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicft1PriSetTimeSlot.setStatus('current')
hpnicft1DChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1DChannelIndex.setStatus('current')
hpnicft1SubScribLineChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1SubScribLineChannelIndex.setStatus('current')
hpnicft1InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3), )
if mibBuilder.loadTexts: hpnicft1InterfaceTable.setStatus('current')
hpnicft1InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicft1InterfaceEntry.setStatus('current')
hpnicft1ControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicft1ControllerIndex.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-T1-MIB", hpnicft1InterfaceInCrcErrs=hpnicft1InterfaceInCrcErrs, hpnicft1LineCode=hpnicft1LineCode, hpnicft1InterfaceEntry=hpnicft1InterfaceEntry, hpnicft1ControllerIndex=hpnicft1ControllerIndex, hpnicft1InterfaceInFramingErrs=hpnicft1InterfaceInFramingErrs, hpnicft1InterfaceInAlignErrs=hpnicft1InterfaceInAlignErrs, hpnicft1FrameFormat=hpnicft1FrameFormat, hpnicft1DChannelIndex=hpnicft1DChannelIndex, hpnicft1InterfaceOutDeferedErrs=hpnicft1InterfaceOutDeferedErrs, hpnicft1Table=hpnicft1Table, hpnicft1SubScribLineChannelIndex=hpnicft1SubScribLineChannelIndex, hpnicft1Type=hpnicft1Type, hpnicft1InterfaceStatusEntry=hpnicft1InterfaceStatusEntry, hpnicft1InterfaceOutUnderRunErrs=hpnicft1InterfaceOutUnderRunErrs, hpnicft1InterfaceStatusTable=hpnicft1InterfaceStatusTable, hpnicft1Clock=hpnicft1Clock, hpnicft1InterfaceOutputErrs=hpnicft1InterfaceOutputErrs, hpnicft1InterfaceOutCollisonsErrs=hpnicft1InterfaceOutCollisonsErrs, hpnicft1InterfaceInNoBufferErrs=hpnicft1InterfaceInNoBufferErrs, hpnicft1InterfaceInDribblesErrs=hpnicft1InterfaceInDribblesErrs, HpnicfT1TimeSlot=HpnicfT1TimeSlot, hpnicfT1=hpnicfT1, hpnicft1InterfaceInRuntsErrs=hpnicft1InterfaceInRuntsErrs, hpnicft1InterfaceInGiantsErrs=hpnicft1InterfaceInGiantsErrs, hpnicft1InterfaceInAbortedSeqErrs=hpnicft1InterfaceInAbortedSeqErrs, PYSNMP_MODULE_ID=hpnicfT1, hpnicft1Entry=hpnicft1Entry, hpnicft1InterfaceInOverRunsErrs=hpnicft1InterfaceInOverRunsErrs, hpnicft1InterfaceInErrs=hpnicft1InterfaceInErrs, hpnicft1PriSetTimeSlot=hpnicft1PriSetTimeSlot, hpnicft1InterfaceTable=hpnicft1InterfaceTable)