#
# PySNMP MIB module CISCO-FC-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FC-SPAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter64, Bits, TimeTicks, MibIdentifier, Unsigned32, Counter32, IpAddress, ObjectIdentity, Gauge32, NotificationType, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "TimeTicks", "MibIdentifier", "Unsigned32", "Counter32", "IpAddress", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFcSpanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 363))
ciscoFcSpanMIB.setRevisions(('2003-04-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFcSpanMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFcSpanMIB.setLastUpdated('200304090000Z')
if mibBuilder.loadTexts: ciscoFcSpanMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoFcSpanMIB.setContactInfo('Cisco Systems Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFcSpanMIB.setDescription('MIB module for displaying and configuring Switched Port Analyzer(SPAN) related features in a Fibre Channel device. SPAN is a feature that enables the user to analyze network traffic, passing through the ports (called SPAN source ports) in a switched network using SwitchProbe device attached to a switch port called SPAN destination (SD) port. SPAN feature is non- intrusive and does not affect switching of network traffic for any of the source ports.')
ciscoSpanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 363, 1))
cspanConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1))
class SessionIndex(TextualConvention, Unsigned32):
    description = 'An arbitrary value which identifies a session. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4095)

cspanMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanMaxSessions.setStatus('current')
if mibBuilder.loadTexts: cspanMaxSessions.setDescription('Maximum number of SPAN sessions that this device supports.')
cspanSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2), )
if mibBuilder.loadTexts: cspanSessionTable.setStatus('current')
if mibBuilder.loadTexts: cspanSessionTable.setDescription('cspanSessionTable is a table that lets the user configure and monitor the SPAN sessions. A SPAN session represents an association of one destination port with traffic redirected from different interfaces and VSANs (Virtual Storage Area Networks). In most situations, there would be only one active session. The flexibility to configure multiple sessions is helpful in sharing the analyzer that is attached to the SPAN destination port. In other words, the user can configure multiple sessions, but only one is active. However, it is possible to have multiple session active at a given time. The traffic on the SPAN destination port is the result of the combination of the active sessions.')
cspanSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"))
if mibBuilder.loadTexts: cspanSessionEntry.setStatus('current')
if mibBuilder.loadTexts: cspanSessionEntry.setDescription('A SPAN session entry. Each session consists of session number, session Administrative Status session OperationStatus, session InactiveReason (if the session OperationStatus is Inactive) and a rowStatus object to add/delete sessions. cspanSessionIndex is the Index of this table that identifies a session. To Add a session: 1. Specify the session to be added (cspanSessionIndex) 2. Set the cspanSessionRowStatus to createAndGo (4). To Delete a session: 1. Specify the session to be deleted (cspanSessionIndex). 2. Set the cspanSessionRowStatus to destroy (6). ')
cspanSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 1), SessionIndex())
if mibBuilder.loadTexts: cspanSessionIndex.setStatus('current')
if mibBuilder.loadTexts: cspanSessionIndex.setDescription('An arbitrary value which identifies a session. The value of this index must be less than the value of cspanMaxSessions.')
cspanSessionDestIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cspanSessionDestIfIndex.setStatus('current')
if mibBuilder.loadTexts: cspanSessionDestIfIndex.setDescription('The ifIndex of the destination port to be configured for the session specified by the instance of cspanSessionIndex.')
cspanSessionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cspanSessionAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cspanSessionAdminStatus.setDescription("This object is used to suspend an active session or activate an inactive session. Note that setting the value to the existing value has no effect on the operation. i.e. setting the value to 'active' when session is 'active' has no effect.")
cspanSessionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanSessionOperStatus.setStatus('current')
if mibBuilder.loadTexts: cspanSessionOperStatus.setDescription('The current state of the session. ')
cspanSessionInactiveReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanSessionInactiveReason.setStatus('current')
if mibBuilder.loadTexts: cspanSessionInactiveReason.setDescription('The description of the reason that this session is not active. This string will be a zero length string in case the session is active.')
cspanSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cspanSessionRowStatus.setStatus('current')
if mibBuilder.loadTexts: cspanSessionRowStatus.setDescription('Status of this row.')
cspanSourcesIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3), )
if mibBuilder.loadTexts: cspanSourcesIfTable.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesIfTable.setDescription('The cspanSourcesIfTable is used to configure source interfaces for SPAN sessions.')
cspanSourcesIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"), (0, "CISCO-FC-SPAN-MIB", "cspanSourcesIfIndex"), (0, "CISCO-FC-SPAN-MIB", "cspanSourcesDirection"))
if mibBuilder.loadTexts: cspanSourcesIfEntry.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesIfEntry.setDescription('A SPAN source interface entry. Each entry consists of session index, interface index of the source interface, the ingress or egress direction of the traffic on that interface and a rowStatus object')
cspanSourcesIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cspanSourcesIfIndex.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesIfIndex.setDescription('cspanSourcesIfIndex denotes the interface index for this session.')
cspanSourcesDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("transmit", 2))))
if mibBuilder.loadTexts: cspanSourcesDirection.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesDirection.setDescription('cspanSourcesDirection denotes traffic direction on the cspanSourcesIfIndex.')
cspanSourcesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cspanSourcesRowStatus.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesRowStatus.setDescription('Status of this row.')
cspanSourcesVsanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4), )
if mibBuilder.loadTexts: cspanSourcesVsanTable.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanTable.setDescription('The cspanSourcesVsanTable is used to list source VSANs for SPAN sessions.')
cspanSourcesVsanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"))
if mibBuilder.loadTexts: cspanSourcesVsanEntry.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanEntry.setDescription('An entry in the Source VSAN Table. For the session identified by the instance of cspanSessionIndex, it lists the VSANs that comprise the sources.')
cspanSourcesVsans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1, 1), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanSourcesVsans2k.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsans2k.setDescription("The VSANs that are traffic sources to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 1 through 8, the second octet specifying VSAN 9 through 16, etc. Since there are 256 octets, the range of VSANs is from 0-2047. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'. ")
cspanSourcesVsans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1, 2), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanSourcesVsans4k.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsans4k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 2048 through 2055, the second octet specifying VSAN 2056 through 2063, etc. Since there are 256 octets, he range of VSANs is from 2048 through 4095. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanSourcesVsanCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5), )
if mibBuilder.loadTexts: cspanSourcesVsanCfgTable.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgTable.setDescription('The cspanSourcesVsanCfgTable is used to configure sources VSANs for SPAN sessions. ')
cspanSourcesVsanCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgSessIndex"))
if mibBuilder.loadTexts: cspanSourcesVsanCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgEntry.setDescription('An entry in the source Vsan Configuration Table. Each entry represents either an add or a delete VSANs operation for the session identified by the instance of cspanSourcesVsanCfgSessIndex. The VSANs to be added (or deleted) are specified by the values of cspanSourcesVsanCfgVsans2k and cspanSourcesVsanCfgVsans4k.')
cspanSourcesVsanCfgSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 1), SessionIndex())
if mibBuilder.loadTexts: cspanSourcesVsanCfgSessIndex.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgSessIndex.setDescription('A session index associated with a session for which the VSANs are to be added/deleted. ')
cspanSourcesVsanCfgCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("remove", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanSourcesVsanCfgCommand.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgCommand.setDescription("The command to be executed for this entry. Only acceptable commands are 'add' and 'remove'. 'none' is returned in case of read operation.")
cspanSourcesVsanCfgVsans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 3), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanSourcesVsanCfgVsans2k.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgVsans2k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 1 through 8, the second octet specifying VSAN 9 through 16, etc. Since there are 256 octets, the range of VSANs is from 0-2047. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanSourcesVsanCfgVsans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 4), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanSourcesVsanCfgVsans4k.setStatus('current')
if mibBuilder.loadTexts: cspanSourcesVsanCfgVsans4k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 2048 through 2055, the second octet specifying VSAN 2056 through 2063, etc. The range of VSANs is 2048-4095. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanVsanFilterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6), )
if mibBuilder.loadTexts: cspanVsanFilterTable.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterTable.setDescription('The cspanVsanFilterTable is used to monitor and configure VSAN filters for SPAN sessions. cspanVsanFilterSessIndex denotes the session index of this sesion. cspanVsanFilterVsans2k and cspanVsanFilterVsans4k denote the VSANs in a bit mask fashion for each session. ')
cspanVsanFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanVsanFilterSessIndex"))
if mibBuilder.loadTexts: cspanVsanFilterEntry.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterEntry.setDescription('An entry in the VsanFilter Table. cspanVsanFilterVsans2k and cspanVsanFilterVsans4k denote the VSANs that are part of the filter applied to the session identified by the instance of cspanVsanFilterSessIndex.')
cspanVsanFilterSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 1), SessionIndex())
if mibBuilder.loadTexts: cspanVsanFilterSessIndex.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterSessIndex.setDescription('A session index associated with a session. ')
cspanVsanFilterVsans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 2), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanVsanFilterVsans2k.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterVsans2k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 1 through 8, the second octet specifying VSAN 9 through 16, etc. Since there are 256 octets, the range of VSANs is from 0-2047. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanVsanFilterVsans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 3), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cspanVsanFilterVsans4k.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterVsans4k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 2048 through 2055, the second octet specifying VSAN 2056 through 2063, etc. the range of VSANs is 2048-4095. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanVsanFilterOpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7), )
if mibBuilder.loadTexts: cspanVsanFilterOpTable.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpTable.setDescription('cspanVsanFilterOpTable is used to configure VSAN filters for SPAN sessions. cspanVsanFilterSessIndex denotes the session index of this sesion. cspanVsanFilterVsans denotes the VSANs in a bit mask fashion for each session. ')
cspanVsanFilterOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-FC-SPAN-MIB", "cspanVsanFilterOpSessIndex"))
if mibBuilder.loadTexts: cspanVsanFilterOpEntry.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpEntry.setDescription('An entry in the VsanFilterOp Table. ')
cspanVsanFilterOpSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 1), SessionIndex())
if mibBuilder.loadTexts: cspanVsanFilterOpSessIndex.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpSessIndex.setDescription('A session index associated with a session. ')
cspanVsanFilterOpCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("remove", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanVsanFilterOpCommand.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpCommand.setDescription('The command to be executed for this entry.')
cspanVsanFilterOpVsans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 3), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanVsanFilterOpVsans2k.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpVsans2k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 1 through 8, the second octet specifying VSAN 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
cspanVsanFilterOpVsans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 4), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cspanVsanFilterOpVsans4k.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpVsans4k.setDescription("The VSANs that are assigned to this session. Each octet within the value of this object specifies a set of eight VSANS with the first octet specifying VSAN 2048 through 2055, the second octet specifying VSAN 2056 through 2063, etc. In each octet, the most significant bit represents the lowest numbered VSAN id and the least significant bit represents the highest numbered VSAN id. Thus each VSAN is represented by a single bit within the value of this object. If that bit has value '1' then that VSAN is included in the set of VSANs; the VSAN is not included if its bit has a value of '0'.")
ciscoFcSpanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 363, 2))
ciscoFcSpanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 1))
ciscoFcSpanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2))
ciscoFcSpanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 1, 1)).setObjects(("CISCO-FC-SPAN-MIB", "cspanScalarsGroup"), ("CISCO-FC-SPAN-MIB", "cspanSessionsGroup"), ("CISCO-FC-SPAN-MIB", "cspanSourceIfGroup"), ("CISCO-FC-SPAN-MIB", "cspanSourceVsanGroup"), ("CISCO-FC-SPAN-MIB", "cspanSourceVsanCfgGroup"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterGroup"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcSpanMIBCompliance = ciscoFcSpanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFcSpanMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-FC-SPAN-MIB.')
cspanScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 1)).setObjects(("CISCO-FC-SPAN-MIB", "cspanMaxSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanScalarsGroup = cspanScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: cspanScalarsGroup.setDescription('A collection of scalar objects in this MIB.')
cspanSessionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 2)).setObjects(("CISCO-FC-SPAN-MIB", "cspanSessionDestIfIndex"), ("CISCO-FC-SPAN-MIB", "cspanSessionAdminStatus"), ("CISCO-FC-SPAN-MIB", "cspanSessionOperStatus"), ("CISCO-FC-SPAN-MIB", "cspanSessionInactiveReason"), ("CISCO-FC-SPAN-MIB", "cspanSessionRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanSessionsGroup = cspanSessionsGroup.setStatus('current')
if mibBuilder.loadTexts: cspanSessionsGroup.setDescription('A collection of objects for sessions configuration.')
cspanSourceIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 3)).setObjects(("CISCO-FC-SPAN-MIB", "cspanSourcesRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanSourceIfGroup = cspanSourceIfGroup.setStatus('current')
if mibBuilder.loadTexts: cspanSourceIfGroup.setDescription('A collection of objects for source interface configuration.')
cspanSourceVsanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 4)).setObjects(("CISCO-FC-SPAN-MIB", "cspanSourcesVsans2k"), ("CISCO-FC-SPAN-MIB", "cspanSourcesVsans4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanSourceVsanGroup = cspanSourceVsanGroup.setStatus('current')
if mibBuilder.loadTexts: cspanSourceVsanGroup.setDescription('A collection of objects for source VSANs display.')
cspanSourceVsanCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 5)).setObjects(("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgCommand"), ("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans2k"), ("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanSourceVsanCfgGroup = cspanSourceVsanCfgGroup.setStatus('current')
if mibBuilder.loadTexts: cspanSourceVsanCfgGroup.setDescription('A collection of objects for source VSANs configuration.')
cspanVsanFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 6)).setObjects(("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans2k"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterVsans2k"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterVsans4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanVsanFilterGroup = cspanVsanFilterGroup.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterGroup.setDescription('A collection of objects for filter display information.')
cspanVsanFilterOpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 7)).setObjects(("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpCommand"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpVsans2k"), ("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpVsans4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cspanVsanFilterOpGroup = cspanVsanFilterOpGroup.setStatus('current')
if mibBuilder.loadTexts: cspanVsanFilterOpGroup.setDescription('A collection of objects for filter operations.')
mibBuilder.exportSymbols("CISCO-FC-SPAN-MIB", ciscoFcSpanMIBConformance=ciscoFcSpanMIBConformance, ciscoFcSpanMIBCompliances=ciscoFcSpanMIBCompliances, cspanVsanFilterEntry=cspanVsanFilterEntry, cspanSessionTable=cspanSessionTable, cspanSourcesVsanTable=cspanSourcesVsanTable, cspanSourcesRowStatus=cspanSourcesRowStatus, cspanVsanFilterVsans4k=cspanVsanFilterVsans4k, cspanSourcesIfEntry=cspanSourcesIfEntry, cspanSourcesVsanCfgVsans4k=cspanSourcesVsanCfgVsans4k, cspanSessionDestIfIndex=cspanSessionDestIfIndex, cspanMaxSessions=cspanMaxSessions, cspanVsanFilterOpVsans2k=cspanVsanFilterOpVsans2k, cspanSessionAdminStatus=cspanSessionAdminStatus, cspanSourcesIfTable=cspanSourcesIfTable, cspanVsanFilterOpVsans4k=cspanVsanFilterOpVsans4k, ciscoFcSpanMIBGroups=ciscoFcSpanMIBGroups, cspanSourceIfGroup=cspanSourceIfGroup, cspanSessionOperStatus=cspanSessionOperStatus, cspanSessionInactiveReason=cspanSessionInactiveReason, cspanSourcesVsans2k=cspanSourcesVsans2k, cspanVsanFilterOpGroup=cspanVsanFilterOpGroup, PYSNMP_MODULE_ID=ciscoFcSpanMIB, cspanVsanFilterTable=cspanVsanFilterTable, cspanVsanFilterGroup=cspanVsanFilterGroup, cspanSourcesVsanCfgSessIndex=cspanSourcesVsanCfgSessIndex, cspanSessionRowStatus=cspanSessionRowStatus, cspanSourcesVsanCfgEntry=cspanSourcesVsanCfgEntry, cspanScalarsGroup=cspanScalarsGroup, SessionIndex=SessionIndex, cspanSourcesVsans4k=cspanSourcesVsans4k, ciscoFcSpanMIB=ciscoFcSpanMIB, cspanSessionsGroup=cspanSessionsGroup, cspanSourcesVsanEntry=cspanSourcesVsanEntry, cspanVsanFilterSessIndex=cspanVsanFilterSessIndex, cspanSessionIndex=cspanSessionIndex, cspanConfiguration=cspanConfiguration, cspanVsanFilterOpTable=cspanVsanFilterOpTable, cspanVsanFilterOpEntry=cspanVsanFilterOpEntry, cspanVsanFilterOpCommand=cspanVsanFilterOpCommand, cspanSourceVsanCfgGroup=cspanSourceVsanCfgGroup, cspanSourcesIfIndex=cspanSourcesIfIndex, cspanSourcesVsanCfgTable=cspanSourcesVsanCfgTable, cspanSourcesVsanCfgCommand=cspanSourcesVsanCfgCommand, ciscoFcSpanMIBCompliance=ciscoFcSpanMIBCompliance, cspanSourceVsanGroup=cspanSourceVsanGroup, cspanSessionEntry=cspanSessionEntry, cspanSourcesDirection=cspanSourcesDirection, ciscoSpanMIBObjects=ciscoSpanMIBObjects, cspanSourcesVsanCfgVsans2k=cspanSourcesVsanCfgVsans2k, cspanVsanFilterOpSessIndex=cspanVsanFilterOpSessIndex, cspanVsanFilterVsans2k=cspanVsanFilterVsans2k)