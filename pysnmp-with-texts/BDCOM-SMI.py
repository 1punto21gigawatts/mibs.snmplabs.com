#
# PySNMP MIB module BDCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BDCOM-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:36:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, Counter32, Unsigned32, Gauge32, TimeTicks, IpAddress, ModuleIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Counter32", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bdcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320))
if mibBuilder.loadTexts: bdcom.setLastUpdated('20000628Z')
if mibBuilder.loadTexts: bdcom.setOrganization('BDCom, Inc.')
if mibBuilder.loadTexts: bdcom.setContactInfo(' Tel: +86-21-50800666 Postal: No.123,Juli RD,Zhangjiang Hitech Park, Shanghai Baud Data Communication Corporation Inc, Shanghai City 201203, P.R.C ')
if mibBuilder.loadTexts: bdcom.setDescription('Initial version of this MIB module.The Structure of Management Information for the Bdcom enterprise.')
bdcomProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 1))
if mibBuilder.loadTexts: bdcomProducts.setStatus('current')
if mibBuilder.loadTexts: bdcomProducts.setDescription('Bdcom Products is the root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
bdlocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 2))
if mibBuilder.loadTexts: bdlocal.setStatus('current')
if mibBuilder.loadTexts: bdlocal.setDescription('Subtree beneath which pre-10.2 MIBS were built.')
bdtemporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 3))
if mibBuilder.loadTexts: bdtemporary.setStatus('current')
if mibBuilder.loadTexts: bdtemporary.setDescription('Subtree beneath which pre-10.2 experiments were placed.')
bdMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 9))
if mibBuilder.loadTexts: bdMgmt.setStatus('current')
if mibBuilder.loadTexts: bdMgmt.setDescription('bdMgmt is the main subtree for new mib development.')
bdcomModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 12))
if mibBuilder.loadTexts: bdcomModules.setStatus('current')
if mibBuilder.loadTexts: bdcomModules.setDescription('bdcomModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
bdcomPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18))
if mibBuilder.loadTexts: bdcomPolicyAuto.setStatus('current')
if mibBuilder.loadTexts: bdcomPolicyAuto.setDescription('bdcomPolicyAuto is the root of the BDCOM-assigned OID subtree for OIDs which are automatically assigned for use in Policy Management.')
bdcomPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18, 2))
if mibBuilder.loadTexts: bdcomPibToMib.setStatus('current')
if mibBuilder.loadTexts: bdcomPibToMib.setDescription("bdcomPibToMib is the root of the BDCOM-assigned OID subtree for MIBs which are algorithmically generated/translated from BDCOM PIBs with OIDs assigned under the bdcomPIB subtree. These generated MIBs allow management entities (other the current Policy Server) to read the downloaded policy. By convention, for PIB 'bdcomPIB.x', the generated MIB shall have the name 'bdcomPibToMib.x'.")
mibBuilder.exportSymbols("BDCOM-SMI", bdcomModules=bdcomModules, bdcom=bdcom, PYSNMP_MODULE_ID=bdcom, bdcomPolicyAuto=bdcomPolicyAuto, bdMgmt=bdMgmt, bdcomPibToMib=bdcomPibToMib, bdlocal=bdlocal, bdcomProducts=bdcomProducts, bdtemporary=bdtemporary)