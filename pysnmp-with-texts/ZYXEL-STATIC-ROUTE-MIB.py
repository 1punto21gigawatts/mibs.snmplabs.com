#
# PySNMP MIB module ZYXEL-STATIC-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-STATIC-ROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, iso, NotificationType, Integer32, IpAddress, Counter64, MibIdentifier, ObjectIdentity, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "iso", "NotificationType", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelStaticRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77))
if mibBuilder.loadTexts: zyxelStaticRoute.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelStaticRoute.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelStaticRoute.setContactInfo('')
if mibBuilder.loadTexts: zyxelStaticRoute.setDescription('The subtree for static route')
zyxelStaticRouteSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1))
zyStaticRouteMaxNumberOfRoutes = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyStaticRouteMaxNumberOfRoutes.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteMaxNumberOfRoutes.setDescription('The maximum number of static route entries that can be created.')
zyxelStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2), )
if mibBuilder.loadTexts: zyxelStaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: zyxelStaticRouteTable.setDescription('The table cantains static route configuration.')
zyxelStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1), ).setIndexNames((0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteIpAddress"), (0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteSubnetMask"), (0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteGateway"))
if mibBuilder.loadTexts: zyxelStaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelStaticRouteEntry.setDescription('An entry contains static route configuration.')
zyStaticRouteName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStaticRouteName.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteName.setDescription('A descriptive name (up to 10 printable ASCII characters) for identification purposes.')
zyStaticRouteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: zyStaticRouteIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteIpAddress.setDescription('This parameter specifies the IP network address of the final destination. Routing is always based on network number. If you need to specify a route to a single host, use a subnet mask of 255.255.255.255 in the subnet mask field to force the network number to be identical to the host ID.')
zyStaticRouteSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: zyStaticRouteSubnetMask.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteSubnetMask.setDescription('The subnet mask of an IP routing domain that is associated to a static route.')
zyStaticRouteGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 4), IpAddress())
if mibBuilder.loadTexts: zyStaticRouteGateway.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteGateway.setDescription('The IP address of gateway. The gateway is an immediate neighbor of your Switch that will forward the packet to the destination. The gateway must be a router on the same segment as your Switch. ')
zyStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStaticRouteMetric.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteMetric.setDescription('The metric represents the cost of transmission for routing purposes. IP routing uses hop count as the measurement of cost, with a minimum of 1 for directly connected networks. Enter a number that approximates the cost for this link. The number need not be precise, but it must be between 1 and 15. In practice, 2 or 3 is usually a good number.')
zyStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyStaticRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyStaticRouteRowStatus.setDescription('This object allows entries to be created and deleted from the static route table.')
mibBuilder.exportSymbols("ZYXEL-STATIC-ROUTE-MIB", zyStaticRouteRowStatus=zyStaticRouteRowStatus, zyStaticRouteIpAddress=zyStaticRouteIpAddress, zyStaticRouteSubnetMask=zyStaticRouteSubnetMask, zyStaticRouteMetric=zyStaticRouteMetric, zyxelStaticRouteTable=zyxelStaticRouteTable, zyxelStaticRouteSetup=zyxelStaticRouteSetup, zyStaticRouteGateway=zyStaticRouteGateway, zyxelStaticRouteEntry=zyxelStaticRouteEntry, zyxelStaticRoute=zyxelStaticRoute, PYSNMP_MODULE_ID=zyxelStaticRoute, zyStaticRouteMaxNumberOfRoutes=zyStaticRouteMaxNumberOfRoutes, zyStaticRouteName=zyStaticRouteName)