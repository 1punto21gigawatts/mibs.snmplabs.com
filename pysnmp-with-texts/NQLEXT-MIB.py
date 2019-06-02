#
# PySNMP MIB module NQLEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NQLEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:24:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
nqlExt, = mibBuilder.importSymbols("APENT-MIB", "nqlExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, NotificationType, iso, Integer32, Counter32, Counter64, ModuleIdentity, Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
apNqlExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 50, 1))
if mibBuilder.loadTexts: apNqlExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apNqlExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apNqlExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apNqlExtMib.setDescription('The MIB module used to describe the ArrowPoint Communications Network Qualifier Lists (NQLs)')
apNqlTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 50, 2), )
if mibBuilder.loadTexts: apNqlTable.setStatus('current')
if mibBuilder.loadTexts: apNqlTable.setDescription('A list of NQLs')
apNqlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1), ).setIndexNames((0, "NQLEXT-MIB", "apNqlName"))
if mibBuilder.loadTexts: apNqlEntry.setStatus('current')
if mibBuilder.loadTexts: apNqlEntry.setDescription('A group of information uniquely identifying an NQL. One entry exists for each NQL')
apNqlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlStatus.setStatus('current')
if mibBuilder.loadTexts: apNqlStatus.setDescription('Status entry for this row ')
apNqlName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlName.setStatus('current')
if mibBuilder.loadTexts: apNqlName.setDescription('The name of the NQL')
apNqlDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlDescription.setStatus('current')
if mibBuilder.loadTexts: apNqlDescription.setDescription('An NQL description')
apNqlExtTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3), )
if mibBuilder.loadTexts: apNqlExtTable.setStatus('current')
if mibBuilder.loadTexts: apNqlExtTable.setDescription('A list of IP Addresses associated with an NQL')
apNqlExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1), ).setIndexNames((0, "NQLEXT-MIB", "apNqlName"), (0, "NQLEXT-MIB", "apNqlExtAddress"))
if mibBuilder.loadTexts: apNqlExtEntry.setStatus('current')
if mibBuilder.loadTexts: apNqlExtEntry.setDescription('Information uniquely identifying a network address within an NQL')
apNqlExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlExtStatus.setStatus('current')
if mibBuilder.loadTexts: apNqlExtStatus.setDescription('Status entry for this row')
apNqlExtAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlExtAddress.setStatus('current')
if mibBuilder.loadTexts: apNqlExtAddress.setDescription('The IP Address')
apNqlExtPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlExtPrefixLen.setStatus('current')
if mibBuilder.loadTexts: apNqlExtPrefixLen.setDescription('The length of the IP Address Network mask')
apNqlExtDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlExtDescription.setStatus('current')
if mibBuilder.loadTexts: apNqlExtDescription.setDescription('Description of this address range')
apNqlExtLogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apNqlExtLogEnable.setStatus('current')
if mibBuilder.loadTexts: apNqlExtLogEnable.setDescription('Enable logging for address matches')
mibBuilder.exportSymbols("NQLEXT-MIB", apNqlExtEntry=apNqlExtEntry, apNqlDescription=apNqlDescription, apNqlExtTable=apNqlExtTable, apNqlEntry=apNqlEntry, apNqlExtStatus=apNqlExtStatus, PYSNMP_MODULE_ID=apNqlExtMib, apNqlTable=apNqlTable, apNqlName=apNqlName, apNqlExtPrefixLen=apNqlExtPrefixLen, apNqlExtDescription=apNqlExtDescription, apNqlExtAddress=apNqlExtAddress, apNqlExtLogEnable=apNqlExtLogEnable, apNqlStatus=apNqlStatus, apNqlExtMib=apNqlExtMib)