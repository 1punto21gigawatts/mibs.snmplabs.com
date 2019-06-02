#
# PySNMP MIB module HH3C-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Counter64, Bits, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, NotificationType, Gauge32, ObjectIdentity, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Bits", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "MibIdentifier", "iso", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hh3cDns = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 97))
hh3cDns.setRevisions(('2009-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cDns.setRevisionsDescriptions((' ',))
if mibBuilder.loadTexts: hh3cDns.setLastUpdated('200902120000Z')
if mibBuilder.loadTexts: hh3cDns.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cDns.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cDns.setDescription('This MIB contains objects to manage the DNS.')
hh3cDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1))
hh3cDnsStaticSrvIpTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1), )
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpTable.setDescription(' This table is a list of DNS static server IPv4 address configuration, which is manually specified. ')
hh3cDnsStaticSrvIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1), ).setIndexNames((0, "HH3C-DNS-MIB", "hh3cDnsStaticSrvIpType"), (0, "HH3C-DNS-MIB", "hh3cDnsStaticSrvIpAddr"))
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpEntry.setDescription(' An entry of hh3cDnsStaticSrvIpTable. ')
hh3cDnsStaticSrvIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpType.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpType.setDescription(' This node gives the type of the static DNS server IP address. ')
hh3cDnsStaticSrvIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpAddr.setDescription(' This node gives the IP address of the DNS server specified by the user. ')
hh3cDnsStaticSrvIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpPriority.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpPriority.setDescription(' This node gives the priority of the DNS server, according to the creation order. The smaller the value is, the higher the priority level is. ')
hh3cDnsStaticSrvIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpRowStatus.setDescription(' This node gives the operation status of this table entry. ')
hh3cDnsDynamicSrvIpTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2), )
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpTable.setDescription(' This table is a list of DNS dynamic server IPv4 address configuration, which is dynamically obtained through DHCP. ')
hh3cDnsDynamicSrvIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1), ).setIndexNames((0, "HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpType"), (0, "HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpAddr"))
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpEntry.setDescription('An entry of hh3cDnsDynamicSrvIpTable.')
hh3cDnsDynamicSrvIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpType.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpType.setDescription(' This node gives the type of the dynamic DNS server IP address. ')
hh3cDnsDynamicSrvIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpAddr.setDescription(' This node gives the IP address of the DNS server dynamically obtained through DHCP. ')
hh3cDnsDynamicSrvIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpPriority.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpPriority.setDescription(' This node gives the priority of the DNS server, according to the order obtained through DHCP. The smaller the value is, the higher the priority level is. ')
hh3cDnsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2))
hh3cDnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 1))
hh3cDnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 1, 1)).setObjects(("HH3C-DNS-MIB", "hh3cDnsStaticSrvIpGroup"), ("HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cDnsMIBCompliance = hh3cDnsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsMIBCompliance.setDescription(' The compliance statement for entities which implement the DNS MIB. ')
hh3cDnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2))
hh3cDnsStaticSrvIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2, 1)).setObjects(("HH3C-DNS-MIB", "hh3cDnsStaticSrvIpPriority"), ("HH3C-DNS-MIB", "hh3cDnsStaticSrvIpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cDnsStaticSrvIpGroup = hh3cDnsStaticSrvIpGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsStaticSrvIpGroup.setDescription(' A collection of objects providing mandatory DNS server IP addresses manually specified. ')
hh3cDnsDynamicSrvIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2, 2)).setObjects(("HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cDnsDynamicSrvIpGroup = hh3cDnsDynamicSrvIpGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cDnsDynamicSrvIpGroup.setDescription(' A collection of objects providing mandatory DNS server IP addresses dynamically obtained through DHCP. ')
mibBuilder.exportSymbols("HH3C-DNS-MIB", hh3cDnsMIBCompliances=hh3cDnsMIBCompliances, hh3cDnsDynamicSrvIpType=hh3cDnsDynamicSrvIpType, hh3cDnsMIBGroups=hh3cDnsMIBGroups, hh3cDnsObjects=hh3cDnsObjects, hh3cDnsDynamicSrvIpTable=hh3cDnsDynamicSrvIpTable, hh3cDnsStaticSrvIpType=hh3cDnsStaticSrvIpType, hh3cDnsStaticSrvIpEntry=hh3cDnsStaticSrvIpEntry, hh3cDnsStaticSrvIpRowStatus=hh3cDnsStaticSrvIpRowStatus, hh3cDnsStaticSrvIpAddr=hh3cDnsStaticSrvIpAddr, hh3cDnsMIBConformance=hh3cDnsMIBConformance, hh3cDnsDynamicSrvIpAddr=hh3cDnsDynamicSrvIpAddr, hh3cDnsStaticSrvIpPriority=hh3cDnsStaticSrvIpPriority, hh3cDnsStaticSrvIpTable=hh3cDnsStaticSrvIpTable, hh3cDnsDynamicSrvIpPriority=hh3cDnsDynamicSrvIpPriority, hh3cDns=hh3cDns, hh3cDnsDynamicSrvIpEntry=hh3cDnsDynamicSrvIpEntry, hh3cDnsDynamicSrvIpGroup=hh3cDnsDynamicSrvIpGroup, hh3cDnsMIBCompliance=hh3cDnsMIBCompliance, hh3cDnsStaticSrvIpGroup=hh3cDnsStaticSrvIpGroup, PYSNMP_MODULE_ID=hh3cDns)