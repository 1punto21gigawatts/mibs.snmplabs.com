#
# PySNMP MIB module CISCO-DMN-DSG-DPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-DPM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, iso, ModuleIdentity, Counter32, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, Counter64, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "iso", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "Unsigned32", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoDSGDPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36))
ciscoDSGDPM.setRevisions(('2012-03-12 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGDPM.setRevisionsDescriptions(('V01.00.00 2012-03-12 Update for D9854 release R4.',))
if mibBuilder.loadTexts: ciscoDSGDPM.setLastUpdated('201203121700Z')
if mibBuilder.loadTexts: ciscoDSGDPM.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGDPM.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGDPM.setDescription('Cisco generic DPM MIB.')
dpmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 1))
dpmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2))
dpmRegenerate = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("always", 1), ("asNeeded", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmRegenerate.setStatus('current')
if mibBuilder.loadTexts: dpmRegenerate.setDescription('Select whether DPM(Digital Program Mapping) should always regenerate PSI tables, or only when their content has changed.')
dpmGblCfgTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1), )
if mibBuilder.loadTexts: dpmGblCfgTable.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgTable.setDescription('DPM Configuration Table.')
dpmGblCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DPM-MIB", "dpmGblCfgInstanceID"))
if mibBuilder.loadTexts: dpmGblCfgEntry.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgEntry.setDescription('Entry for DPM global configuration table.')
dpmGblCfgInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmGblCfgInstanceID.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgInstanceID.setDescription('DPM Output instance id.')
dpmGblCfgInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgInstanceName.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgInstanceName.setDescription('DPM Output Instance Name.')
dpmGblCfgMapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("svcID", 1), ("svcIDAndPID", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgMapMode.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgMapMode.setDescription('DPM Mode selection.')
dpmGblCfgDupMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("psiRemap", 1), ("packetCopy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgDupMethod.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgDupMethod.setDescription('DPM Program Duplication method selection.')
dpmGblCfgRegenRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("saStandard", 1), ("mpegMinimum", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgRegenRate.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgRegenRate.setDescription('DPM Regeneration rate option selection.')
dpmGblCfgUnrefContent = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("modeI", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgUnrefContent.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgUnrefContent.setDescription('DPM unreferenced content action selection.')
dpmGblCfgPSIOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dropAll", 1), ("passAll", 2), ("ctlByTable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIOutput.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIOutput.setDescription('Program Specific Information table output selection .')
dpmGblCfgSVCIDOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("validChannel", 1), ("allChannel", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgSVCIDOutput.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgSVCIDOutput.setDescription('Specify DPM to Regenerate the Output Only for Valid Service IDs.')
dpmGblCfgPSIPAT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("regeneration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIPAT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIPAT.setDescription('Program Association Table Output selection.')
dpmGblCfgPSICAT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("regeneration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSICAT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSICAT.setDescription('Conditional Access Table Output selection.')
dpmGblCfgPSIPMT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("regeneration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIPMT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIPMT.setDescription('Program Map Table Output selection.')
dpmGblCfgPSITSDT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSITSDT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSITSDT.setDescription('Transport stream description table output selection.')
dpmGblCfgPSINIT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("regeneration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSINIT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSINIT.setDescription('Network Information table output selection.')
dpmGblCfgPSINITO = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("pwRC", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSINITO.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSINITO.setDescription('NITO output selection.')
dpmGblCfgPSISDT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("regeneration", 3), ("pwRC", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSISDT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSISDT.setDescription('Service description table selection.')
dpmGblCfgPSISDTO = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("pwRC", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSISDTO.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSISDTO.setDescription('SDTO output selection.')
dpmGblCfgPSIBAT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("pwRC", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIBAT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIBAT.setDescription('Bouquet Association Table output selection.')
dpmGblCfgPSIEIT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIEIT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIEIT.setDescription('Event Information Table output selection.')
dpmGblCfgPSITDT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSITDT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSITDT.setDescription('Time and Data Table output selection.')
dpmGblCfgPSIST = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIST.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIST.setDescription('Stuffing Table output selection.')
dpmGblCfgPSIRST = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIRST.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIRST.setDescription('Running status Table output selection.')
dpmGblCfgPSITOT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSITOT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSITOT.setDescription('Time Offset Table output selection.')
dpmGblCfgPSIDIT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIDIT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIDIT.setDescription('Discontinuity information Table output selection.')
dpmGblCfgPSISIT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSISIT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSISIT.setDescription('Selection information Table output selection.')
dpmGblCfgPSIECM = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIECM.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIECM.setDescription('Entitlement Control message output selection.')
dpmGblCfgPSIEMM = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIEMM.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIEMM.setDescription('Entitlement Management message output selection.')
dpmGblCfgPSIDRT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSIDRT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSIDRT.setDescription('Disaster Recovery Table output selection.')
dpmGblCfgPSICDT = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPSICDT.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPSICDT.setDescription('Code Download Table output selection.')
dpmGblCfgPATPMTOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgPATPMTOffset.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgPATPMTOffset.setDescription('Mode-i PAT and PMT offset. Only applicable if Unreferenced Content is set to mode-i.')
dpmGblCfgNITOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmGblCfgNITOffset.setStatus('current')
if mibBuilder.loadTexts: dpmGblCfgNITOffset.setDescription('Mode-i NIT offset. Only applicable if Unreferenced Content is set to mode-i.')
dpmPeMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2), )
if mibBuilder.loadTexts: dpmPeMappingTable.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingTable.setDescription('DPM Program Entry Table.')
dpmPeMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DPM-MIB", "dpmPeMappingInstanceID"), (0, "CISCO-DMN-DSG-DPM-MIB", "dpmPeMappingPEID"))
if mibBuilder.loadTexts: dpmPeMappingEntry.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingEntry.setDescription('Entry for DPM PE Mapping Entry table.')
dpmPeMappingInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmPeMappingInstanceID.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingInstanceID.setDescription('DPM Output Instance id.')
dpmPeMappingPEID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmPeMappingPEID.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingPEID.setDescription('DPM Program Entry id.')
dpmPeMappingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("drop", 1), ("pass", 2), ("map", 3), ("xcode", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPeMappingAction.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingAction.setDescription('DPM Program Entry Action Selection.')
dpmPeMappingPMTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPeMappingPMTPID.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingPMTPID.setDescription('DPM Output Program Map Table PID.')
dpmPeMappingOpChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPeMappingOpChannel.setStatus('current')
if mibBuilder.loadTexts: dpmPeMappingOpChannel.setDescription('DPM Output Service Id selection.')
dpmPIDMapTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3), )
if mibBuilder.loadTexts: dpmPIDMapTable.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapTable.setDescription('DPM PID Map Entry Table.')
dpmPIDMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DPM-MIB", "dpmPIDMapIndex"))
if mibBuilder.loadTexts: dpmPIDMapEntry.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapEntry.setDescription('Entry for DPM PE Mapping Entry table. No of Entries for D9858 : 200 No of Entries for D9854 : 200 No of Entries for D9854-I: 768 No of Entries for D9824 : 768 ')
dpmPIDMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 768))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmPIDMapIndex.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapIndex.setDescription('Program ID Mapping Output Index.')
dpmPIDMapInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapInstanceID.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapInstanceID.setDescription('Program ID Mapping Output Instance Id selection.')
dpmPIDMapPEID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapPEID.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapPEID.setDescription('Program ID Mapping Program Entry ID selection.')
dpmPIDMapRow = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapRow.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapRow.setDescription('Selection of Row in Program Map Table.')
dpmPIDMapStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapStreamType.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapStreamType.setDescription('Selection of Raw Stream Type in Program Map Table Only used when dpmPIDMapStreamCategory is set to ukn().')
dpmPIDMapStreamCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("invl", 1), ("pcr", 2), ("vid", 3), ("aud", 4), ("subt", 5), ("vbi", 6), ("dpi", 7), ("mpe", 8), ("ttx", 9), ("data", 10), ("lsdt", 11), ("cdt", 12), ("etv", 13), ("ukn", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapStreamCategory.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapStreamCategory.setDescription('Selection of stream category.')
dpmPIDMapStreamInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapStreamInstance.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapStreamInstance.setDescription('Selection of stream instance.')
dpmPIDMapAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("drop", 1), ("map", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapAction.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapAction.setDescription('Selection of Program ID Mapping selection.')
dpmPIDMapOutputPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapOutputPID.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapOutputPID.setDescription(' Output PID.')
dpmPIDMapInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 3, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpmPIDMapInuse.setStatus('current')
if mibBuilder.loadTexts: dpmPIDMapInuse.setDescription('PID Mapping in use.')
dpmAlignedPMTTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4), )
if mibBuilder.loadTexts: dpmAlignedPMTTable.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTTable.setDescription('DPM Aligned PMT Table.')
dpmAlignedPMTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTInstanceID"), (0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTPEID"), (0, "CISCO-DMN-DSG-DPM-MIB", "dpmAlignedPMTRow"))
if mibBuilder.loadTexts: dpmAlignedPMTEntry.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTEntry.setDescription('Entry for DPM Aligned PMT table.')
dpmAlignedPMTInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmAlignedPMTInstanceID.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTInstanceID.setDescription('Aligned Program Map Table Instance ID .')
dpmAlignedPMTPEID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmAlignedPMTPEID.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTPEID.setDescription('Aligned Program Map Table Program Entry ID .')
dpmAlignedPMTRow = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmAlignedPMTRow.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTRow.setDescription('Aligned Program Map Table Row .')
dpmAlignedPMTStreamTypeTxt = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmAlignedPMTStreamTypeTxt.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTStreamTypeTxt.setDescription(' Type of Stream .')
dpmAlignedPMTInputPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 36, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpmAlignedPMTInputPID.setStatus('current')
if mibBuilder.loadTexts: dpmAlignedPMTInputPID.setDescription('Input PID .')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DPM-MIB", dpmGblCfgPSIEIT=dpmGblCfgPSIEIT, dpmRegenerate=dpmRegenerate, dpmPIDMapTable=dpmPIDMapTable, dpmGblCfgPSIPMT=dpmGblCfgPSIPMT, dpmGblCfgInstanceName=dpmGblCfgInstanceName, dpmGblCfgTable=dpmGblCfgTable, dpmGblCfgPSIRST=dpmGblCfgPSIRST, dpmGblCfgPSIDRT=dpmGblCfgPSIDRT, dpmGblCfgPSICAT=dpmGblCfgPSICAT, dpmGblCfgPSIDIT=dpmGblCfgPSIDIT, dpmPIDMapInuse=dpmPIDMapInuse, dpmPeMappingAction=dpmPeMappingAction, dpmGblCfgRegenRate=dpmGblCfgRegenRate, dpmGblCfgPSITDT=dpmGblCfgPSITDT, dpmPeMappingPMTPID=dpmPeMappingPMTPID, dpmPeMappingOpChannel=dpmPeMappingOpChannel, PYSNMP_MODULE_ID=ciscoDSGDPM, dpmPeMappingPEID=dpmPeMappingPEID, dpmGblCfgPATPMTOffset=dpmGblCfgPATPMTOffset, dpmGblCfgMapMode=dpmGblCfgMapMode, dpmAlignedPMTPEID=dpmAlignedPMTPEID, dpmGblCfgPSITSDT=dpmGblCfgPSITSDT, dpmPIDMapAction=dpmPIDMapAction, dpmPIDMapStreamCategory=dpmPIDMapStreamCategory, dpmAlignedPMTInputPID=dpmAlignedPMTInputPID, dpmAlignedPMTInstanceID=dpmAlignedPMTInstanceID, dpmGblCfgEntry=dpmGblCfgEntry, dpmTable=dpmTable, dpmGblCfgPSIPAT=dpmGblCfgPSIPAT, dpmPIDMapStreamInstance=dpmPIDMapStreamInstance, dpmGblCfgDupMethod=dpmGblCfgDupMethod, dpmAlignedPMTTable=dpmAlignedPMTTable, dpmGblCfgPSICDT=dpmGblCfgPSICDT, dpmGblCfgNITOffset=dpmGblCfgNITOffset, dpmGblCfgPSISIT=dpmGblCfgPSISIT, dpmGblCfgPSIOutput=dpmGblCfgPSIOutput, dpmGblCfgPSITOT=dpmGblCfgPSITOT, ciscoDSGDPM=ciscoDSGDPM, dpmGblCfgPSIECM=dpmGblCfgPSIECM, dpmGblCfgPSISDTO=dpmGblCfgPSISDTO, dpmPeMappingTable=dpmPeMappingTable, dpmPeMappingInstanceID=dpmPeMappingInstanceID, dpmPIDMapInstanceID=dpmPIDMapInstanceID, dpmAlignedPMTRow=dpmAlignedPMTRow, dpmInfo=dpmInfo, dpmGblCfgSVCIDOutput=dpmGblCfgSVCIDOutput, dpmPIDMapPEID=dpmPIDMapPEID, dpmAlignedPMTStreamTypeTxt=dpmAlignedPMTStreamTypeTxt, dpmGblCfgUnrefContent=dpmGblCfgUnrefContent, dpmPIDMapOutputPID=dpmPIDMapOutputPID, dpmPIDMapIndex=dpmPIDMapIndex, dpmPIDMapStreamType=dpmPIDMapStreamType, dpmGblCfgPSISDT=dpmGblCfgPSISDT, dpmGblCfgPSINITO=dpmGblCfgPSINITO, dpmGblCfgPSIBAT=dpmGblCfgPSIBAT, dpmGblCfgPSINIT=dpmGblCfgPSINIT, dpmGblCfgPSIEMM=dpmGblCfgPSIEMM, dpmPIDMapEntry=dpmPIDMapEntry, dpmGblCfgInstanceID=dpmGblCfgInstanceID, dpmPIDMapRow=dpmPIDMapRow, dpmGblCfgPSIST=dpmGblCfgPSIST, dpmAlignedPMTEntry=dpmAlignedPMTEntry, dpmPeMappingEntry=dpmPeMappingEntry)