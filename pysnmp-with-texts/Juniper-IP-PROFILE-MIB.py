#
# PySNMP MIB module Juniper-IP-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-PROFILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:03:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, JuniName, JuniSetMap = mibBuilder.importSymbols("Juniper-TC", "JuniEnable", "JuniName", "JuniSetMap")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Bits, Gauge32, ObjectIdentity, Integer32, TimeTicks, Counter32, MibIdentifier, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Bits", "Gauge32", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
juniIpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26))
juniIpProfileMIB.setRevisions(('2006-09-08 10:26', '2005-09-13 17:21', '2004-10-05 14:04', '2003-09-24 15:33', '2002-10-11 13:20', '2001-01-24 20:06', '2000-05-08 00:00', '1999-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpProfileMIB.setRevisionsDescriptions(('Added support for Blocking multicast sources on IP Interfaces - juniIpProfileBlockMulticastSources.', 'Added support for Flow Stats a.k.a. J-Flow for IP Interfaces by including juniIpProfileFlowStats.', 'Added support for IP filter options all for IP Interfaces by including juniIpProfileFilterOptionsAll.', 'Added support for TCP MSS configuration for IP interfaces by including juniIpProfileTcpMss.', 'Replaced Unisphere names with Juniper names. In juniIpProfileTable, to support unnumbered interfaces referencing numbered interfaces in addition to loopback interfaces, the following object is made obsolete: juniIpProfileLoopback and the following object is added: juniIpProfileInheritNumString', 'Deprecated juniIpProfileRowStatus; the table is now dense and populated as a side-effect of creation of an entry in the juniProfileNameTable in Juniper-PROFILE-MIB. Also, added juniIpProfileSetMap and juniIpProfileSrcAddrValidEnable.', 'Obsoleted juniIpProfileLoopbackIfIndex, replacing it with juniIpProfileLoopback.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniIpProfileMIB.setLastUpdated('200609081026Z')
if mibBuilder.loadTexts: juniIpProfileMIB.setOrganization('Juniper Networks')
if mibBuilder.loadTexts: juniIpProfileMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpProfileMIB.setDescription('The IP Profile MIB for the Juniper Networks enterprise.')
juniIpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1))
juniIpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1))
juniIpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1), )
if mibBuilder.loadTexts: juniIpProfileTable.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileTable.setDescription('The entries in this table describe profiles for configuring IP interfaces. Entries in this table are created/deleted as a side-effect of corresponding operations to the juniProfileNameTable in the Juniper-PROFILE-MIB.')
juniIpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-IP-PROFILE-MIB", "juniIpProfileId"))
if mibBuilder.loadTexts: juniIpProfileEntry.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileEntry.setDescription('A profile describing configuration of an IP interface.')
juniIpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniIpProfileId.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileId.setDescription('The integer identifier associated with this profile. A value for this identifier is determined by locating or creating a profile name in the juniProfileNameTable.')
juniIpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRowStatus.setStatus('deprecated')
if mibBuilder.loadTexts: juniIpProfileRowStatus.setDescription("Controls creation/deletion of entries in this table. Only the values 'createAndGo' and 'destroy' may be SET. The value of juniIpProfileId must match that of a profile name configured in juniProfileNameTable.")
juniIpProfileRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 3), JuniName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRouterName.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileRouterName.setDescription('The virtual router to which an IP interface configured by this profile will be assigned, if other mechanisms do not otherwise specify a virtual router assignment.')
juniIpProfileIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpAddr.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileIpAddr.setDescription('An IP address to be used by an IP interface configured by this profile. This object will have a value of 0.0.0.0 for an unnumbered interface.')
juniIpProfileIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpMask.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileIpMask.setDescription('An IP address mask to be used by an IP interface configured by this profile. This object will have a value of 0.0.0.0 for an unnumbered interface.')
juniIpProfileDirectedBcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileDirectedBcastEnable.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileDirectedBcastEnable.setDescription('Enable/disable forwarding of directed broadcasts on this IP network interface.')
juniIpProfileIcmpRedirectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 7), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIcmpRedirectEnable.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileIcmpRedirectEnable.setDescription('Enable/disable transmission of ICMP Redirect messages on this IP network interface.')
juniIpProfileAccessRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 8), JuniEnable().clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileAccessRoute.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileAccessRoute.setDescription('Enable/disable whether a host route is automatically created for a remote host attached to an IP interface that is configured using this profile.')
juniIpProfileMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(512, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileMtu.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileMtu.setDescription('The configured MTU size for this IP network interface. If set to zero, the default MTU size, as determined by the underlying network media, is used.')
juniIpProfileLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopbackIfIndex.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileLoopbackIfIndex.setDescription('For unnumbered interfaces, the IfIndex of the IP loopback interface whose IP address is used as the source address for transmitted IP packets. A value of zero means the loopback interface is unspecified (e.g., when the interface is numbered).')
juniIpProfileLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopback.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileLoopback.setDescription("The number of the loopback interface, associated with the specified virtual router, whose IP address is used as the source address when transmitting IP packets on unnumbered remote access user links. For example, if the loopback interface for the associated router was configured via the console as 'loopback 2', this object would contain the integer value 2. A value of -1 indicates the loopback interface is unspecified, e.g., when the IP interface is numbered. This object has been replaced by juniIpProfileInheritNumString. This object is no longer represented in the juniIpProfileSetMap.")
juniIpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 12), JuniSetMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSetMap.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileSetMap.setDescription("A bitmap representing which objects in this entry have been explicitly configured. See the definition of the JuniSetMap TEXTUAL-CONVENTION for details of use. The INDEX object(s) and this object are excluded from representation (i.e. their bits are never set). When a SET request does not explicitly configure JuniSetMap, bits in JuniSetMap are set as a side-effect of configuring other profile attributes in the same entry. If, however, a SET request explicitly configures JuniSetMap, the explicitly configured value overrides 1) any previous bit settings, and 2) any simultaneous 'side-effect' settings that would otherwise occur. Once set, bits can only be cleared by explicitly configuring JuniSetMap.")
juniIpProfileSrcAddrValidEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 13), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSrcAddrValidEnable.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileSrcAddrValidEnable.setDescription('Enable/disable whether source addresses in received IP packets are validated. Validation is performed by looking up the source IP address in the routing database and determining whether the packet arrived on the expected interface; if not, the packet is discarded.')
juniIpProfileInheritNumString = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileInheritNumString.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileInheritNumString.setDescription("The text identifier of the numbered interface, associated with the specified virtual router, whose IP address is used as the source address when transmitting IP packets on unnumbered remote access user links. Types/formats/examples for this string include: Loopback loopback <id> 'loopback 0' ATM Virtual Circuit atm <slot>/<port>.<distinguisher> 'atm 3/1.100' Ethernet { fastEthernet | gigabitEthernet } <slot>/<port> 'fastEthernet 3/0' 'gigabitEthernet 3/0' Ethernet VLAN { fastEthernet | gigabitEthernet } <slot>/<port>:<vlanID> 'fastEthernet 3/0:1000' 'gigabitEthernet 3/0:1000' Channelized Serial serial <slot>/<port>:<channelSpecifier>[/<channelSpecifier>]* 'serial 3/0:4' (T1/E1) 'serial 3/0:2/4' (T3/E3) 'serial 3/0:2/1/1/4' (OC3/OC12 - channelized DS3) 'serial 3/0:2/1/1/1/4' (OC3/OC12 - virtual tributaries) Other formats may be supported over time. An empty string indicates the referenced interface is unspecified, e.g., when this IP interface is numbered.")
juniIpProfileTcpMss = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(160, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileTcpMss.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileTcpMss.setDescription('Configures TCP MSS value for an IP interface. When configured, MSS value of TCP SYN packets received or transmitted on the interface will be compared with the configured value and lowest of the two will replace the value in the packet.')
juniIpProfileFilterOptionsAll = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 16), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFilterOptionsAll.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileFilterOptionsAll.setDescription('Enable/disable whether IP packets containing options are to be discarded or sent to the control plane for processing.')
juniIpProfileFlowStats = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 17), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFlowStats.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileFlowStats.setDescription('Enable/disable whether J-Flow is enabled on the interface')
juniIpProfileBlockMulticastSources = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 18), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileBlockMulticastSources.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileBlockMulticastSources.setDescription('Enable/disable Blocking Multicast traffic')
juniIpProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4))
juniIpProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1))
juniIpProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2))
juniIpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance = juniIpProfileCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileCompliance.setDescription('Obsolete compliance statement for systems supporting IP configuration profiles. This statement became obsolete when juniIpProfileLoopback replaced juniIpProfileLoopbackIfIndex.')
juniIpProfileCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance1 = juniIpProfileCompliance1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileCompliance1.setDescription('Obsolete compliance statement for systems supporting IP configuration profiles. This statement became obsolete when juniIpProfileRowStatus was deprecate and the juniIpProfileSetMap and juniIpProfileSrcAddrValidEnable objects were added.')
juniIpProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance2 = juniIpProfileCompliance2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileCompliance2.setDescription('Obsolete compliance statement for systems supporting IP configuration profiles. This statement became obsolete when juniIpProfileLoopback was obsoleted and the juniIpProfileInheritNumString object was added.')
juniIpProfileCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance3 = juniIpProfileCompliance3.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileCompliance3.setDescription('Obsolete compliance statement for systems supporting IP configuration profiles. This statement became obsolete when juniIpProfileTcpMss was added.')
juniIpProfileCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance4 = juniIpProfileCompliance4.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileCompliance4.setDescription('Obsolete compliance statement for systems supporting IP configuration profiles. This statement became obsolete when juniIpProfileFilterOptionsAll was added.')
juniIpProfileCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance5 = juniIpProfileCompliance5.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileCompliance5.setDescription('The compliance statement for systems supporting IP configuration profiles, incorporating juniIpProfileFilterOptionsAll.')
juniIpProfileCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance6 = juniIpProfileCompliance6.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileCompliance6.setDescription('The compliance statement for systems supporting IP configuration profiles, incorporating juniIpProfileFlowStats.')
juniIpProfileCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance7 = juniIpProfileCompliance7.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileCompliance7.setDescription('The compliance statement for systems supporting IP configuration profiles, incorporating juniIpProfileBlockMulticastSources.')
juniIpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopbackIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup = juniIpProfileGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This group became obsolete when juniIpProfileLoopback replaced juniIpProfileLoopbackIfIndex.')
juniIpProfileGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup1 = juniIpProfileGroup1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup1.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This group became obsolete when juniIpProfileRowStatus was deprecate and the juniIpProfileSetMap and juniIpProfileSrcAddrValidEnable objects were added.')
juniIpProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup2 = juniIpProfileGroup2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup2.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This statement became obsolete when juniIpProfileLoopback was obsoleted and the juniIpProfileInheritNumString object was added.')
juniIpProfileDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileDeprecatedGroup = juniIpProfileDeprecatedGroup.setStatus('deprecated')
if mibBuilder.loadTexts: juniIpProfileDeprecatedGroup.setDescription('Deprecated object providing management of IP Profile functionality in a Juniper product. This group has been deprecated but may still be supported on some implementations.')
juniIpProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup3 = juniIpProfileGroup3.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup3.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This statement became obsolete when juniIpProfileTcpMss was added.')
juniIpProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup4 = juniIpProfileGroup4.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup4.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This statement became osolete when juniIpProfileFilterOptionsAll was added.')
juniIpProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup5 = juniIpProfileGroup5.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup5.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This statement became osolete when juniIpProfileFlowStats was added.')
juniIpProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup6 = juniIpProfileGroup6.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileGroup6.setDescription('An obsolete collection of objects providing management of IP Profile functionality in a Juniper product. This statement became obsolete when juniIpProfileBlockMulticastSources was added.')
juniIpProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 9)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileBlockMulticastSources"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup7 = juniIpProfileGroup7.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileGroup7.setDescription('The basic collection of objects providing management of IP Profile functionality in a Juniper product.')
mibBuilder.exportSymbols("Juniper-IP-PROFILE-MIB", juniIpProfileCompliance6=juniIpProfileCompliance6, juniIpProfileEntry=juniIpProfileEntry, juniIpProfileObjects=juniIpProfileObjects, juniIpProfileGroup3=juniIpProfileGroup3, juniIpProfileLoopback=juniIpProfileLoopback, juniIpProfile=juniIpProfile, juniIpProfileCompliance=juniIpProfileCompliance, juniIpProfileGroup1=juniIpProfileGroup1, juniIpProfileCompliance7=juniIpProfileCompliance7, juniIpProfileFlowStats=juniIpProfileFlowStats, juniIpProfileGroup5=juniIpProfileGroup5, juniIpProfileLoopbackIfIndex=juniIpProfileLoopbackIfIndex, juniIpProfileIpAddr=juniIpProfileIpAddr, juniIpProfileGroup6=juniIpProfileGroup6, juniIpProfileDirectedBcastEnable=juniIpProfileDirectedBcastEnable, juniIpProfileBlockMulticastSources=juniIpProfileBlockMulticastSources, juniIpProfileCompliance2=juniIpProfileCompliance2, juniIpProfileTcpMss=juniIpProfileTcpMss, juniIpProfileId=juniIpProfileId, PYSNMP_MODULE_ID=juniIpProfileMIB, juniIpProfileMtu=juniIpProfileMtu, juniIpProfileGroup2=juniIpProfileGroup2, juniIpProfileGroup4=juniIpProfileGroup4, juniIpProfileGroup7=juniIpProfileGroup7, juniIpProfileMIBConformance=juniIpProfileMIBConformance, juniIpProfileSetMap=juniIpProfileSetMap, juniIpProfileSrcAddrValidEnable=juniIpProfileSrcAddrValidEnable, juniIpProfileCompliance1=juniIpProfileCompliance1, juniIpProfileIpMask=juniIpProfileIpMask, juniIpProfileCompliance3=juniIpProfileCompliance3, juniIpProfileFilterOptionsAll=juniIpProfileFilterOptionsAll, juniIpProfileTable=juniIpProfileTable, juniIpProfileInheritNumString=juniIpProfileInheritNumString, juniIpProfileCompliance4=juniIpProfileCompliance4, juniIpProfileCompliance5=juniIpProfileCompliance5, juniIpProfileMIB=juniIpProfileMIB, juniIpProfileRouterName=juniIpProfileRouterName, juniIpProfileMIBCompliances=juniIpProfileMIBCompliances, juniIpProfileIcmpRedirectEnable=juniIpProfileIcmpRedirectEnable, juniIpProfileMIBGroups=juniIpProfileMIBGroups, juniIpProfileGroup=juniIpProfileGroup, juniIpProfileRowStatus=juniIpProfileRowStatus, juniIpProfileDeprecatedGroup=juniIpProfileDeprecatedGroup, juniIpProfileAccessRoute=juniIpProfileAccessRoute)