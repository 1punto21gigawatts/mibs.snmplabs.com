#
# PySNMP MIB module DLINK-SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-SWPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:35:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, MibIdentifier, Unsigned32, Bits, Counter64, Gauge32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "Unsigned32", "Bits", "Counter64", "Gauge32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_des30xxproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63)).setLabel("dlink-des30xxproductProd")
dlink_des3010xProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1)).setLabel("dlink-des3010xProd")
dlink_des3010FProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 1)).setLabel("dlink-des3010FProd")
dlink_des3010GProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 2)).setLabel("dlink-des3010GProd")
dlink_des3018Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 2)).setLabel("dlink-des3018Prod")
dlink_des3026Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 3)).setLabel("dlink-des3026Prod")
dlink_des3010FLProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 4)).setLabel("dlink-des3010FLProd")
dlink_des3016Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 10)).setLabel("dlink-des3016Prod")
des30xxSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63))
des3010 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1))
des3010f = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 1))
des3010g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 2))
des3018 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 2))
des3026 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 3))
des3010fl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 4))
des3016 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 10))
mibBuilder.exportSymbols("DLINK-SWPRIMGMT-MIB", dlink_des3018Prod=dlink_des3018Prod, des3018=des3018, des3016=des3016, dlink_des3026Prod=dlink_des3026Prod, dlink_des3010xProd=dlink_des3010xProd, dlink_des3010GProd=dlink_des3010GProd, des30xxSeriesProd=des30xxSeriesProd, dlink_des30xxproductProd=dlink_des30xxproductProd, des3010f=des3010f, des3026=des3026, des3010fl=des3010fl, dlink_des3010FLProd=dlink_des3010FLProd, dlink_des3016Prod=dlink_des3016Prod, dlink_des3010FProd=dlink_des3010FProd, des3010=des3010, des3010g=des3010g)