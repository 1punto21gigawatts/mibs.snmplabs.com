#
# PySNMP MIB module TIARA-PACKETFILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-PACKETFILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, ObjectIdentity, IpAddress, MibIdentifier, Counter64, Integer32, Bits, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "Bits", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
tiaraIpIfIndex, = mibBuilder.importSymbols("TIARA-IP-MIB", "tiaraIpIfIndex")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraPacketFilterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 51))
if mibBuilder.loadTexts: tiaraPacketFilterMib.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: tiaraPacketFilterMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraPacketFilterMib.setContactInfo(' Tiara Networks Customer Service Postal: 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraPacketFilterMib.setDescription("The MIB module to describe Tiara's Packet Filter MIB")
filterRuleClearCounters = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 51, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterRuleClearCounters.setStatus('current')
if mibBuilder.loadTexts: filterRuleClearCounters.setDescription(" This variable is used to clear counters for a given Rule Set Name or All the counters. Whenever a set on this variable is done , the value given by the manager will be interpreted as the filter rule set name for which the counters will be cleared. As a special case if 'all' is the value of this variable then counters corresponding to all the filter rule set names will be cleared.")
filterNameIndexTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 51, 2), )
if mibBuilder.loadTexts: filterNameIndexTable.setStatus('current')
if mibBuilder.loadTexts: filterNameIndexTable.setDescription('This Table maintains a mapping of filter name and Filter Index')
filterNameIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1), ).setIndexNames((0, "TIARA-PACKETFILTER-MIB", "filterNameIndex"))
if mibBuilder.loadTexts: filterNameIndexEntry.setStatus('current')
if mibBuilder.loadTexts: filterNameIndexEntry.setDescription('An entry in the filterRuleNameIndexTable')
filterEntryName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterEntryName.setStatus('current')
if mibBuilder.loadTexts: filterEntryName.setDescription('A unique name for the filter rule')
filterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: filterNameIndex.setStatus('current')
if mibBuilder.loadTexts: filterNameIndex.setDescription('A unique identifier for the filter rule')
filterEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: filterEntryRowStatus.setDescription('Used to add or delete a row in the table')
filterRuleAssignTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 51, 3), )
if mibBuilder.loadTexts: filterRuleAssignTable.setStatus('current')
if mibBuilder.loadTexts: filterRuleAssignTable.setDescription('FilterRuleAssign Table')
filterRuleAssignTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: filterRuleAssignTableEntry.setStatus('current')
if mibBuilder.loadTexts: filterRuleAssignTableEntry.setDescription('An entry in the filterRuleName Table')
filterRuleSetNameIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetNameIn.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetNameIn.setDescription(' Rule Set Name for IN coming Direction')
filterRuleSetNameOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetNameOut.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetNameOut.setDescription(' Rule Set Name for OUT going Direction')
filterRuleAssignTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleAssignTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: filterRuleAssignTableRowStatus.setDescription(' Used to Add or Delete a Row in the table')
filterRuleSetTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4), )
if mibBuilder.loadTexts: filterRuleSetTable.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetTable.setDescription('Filter Rule SetTable')
filterRuleSetTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1), ).setIndexNames((0, "TIARA-PACKETFILTER-MIB", "filterNameIndex"), (0, "TIARA-PACKETFILTER-MIB", "filterRuleSetLineNo"))
if mibBuilder.loadTexts: filterRuleSetTableEntry.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetTableEntry.setDescription('An entry in the Filter Rule Table')
filterRuleSetLineNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: filterRuleSetLineNo.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetLineNo.setDescription(' Line Number where the Rule has to be inserted or an invalid number (0XFFFF) when a row has to be appeded')
filterRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleName.setStatus('current')
if mibBuilder.loadTexts: filterRuleName.setDescription('A unique name for the filter rule')
filterRuleSetAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2), ("reject", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetAction.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetAction.setDescription(' Specifies Action to be taken by the filter when a match occurs to corresponding filter rule')
filterRuleSetProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 17, 0))).clone(namedValues=NamedValues(("icmp", 1), ("tcp", 6), ("udp", 17), ("ip", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetProtocolType.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetProtocolType.setDescription(' where protocol type ip will have value ')
filterRuleSetSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetSrcIpAddr.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetSrcIpAddr.setDescription(' Number of the Source Network')
filterRuleSetSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetSrcMask.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetSrcMask.setDescription(' Wild card Address to be applied to source Address')
filterRuleSetDestIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetDestIpAddr.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetDestIpAddr.setDescription(' Number of the Destination Network')
filterRuleSetDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetDestMask.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetDestMask.setDescription(' Wild card Address to be applied to destination Address')
filterRuleSetPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetPrecedence.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetPrecedence.setDescription('Ip address precedence feild can be used to filter packets')
filterRuleSetTos = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetTos.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetTos.setDescription(' Ip header TOS feild can be used to filter the packets')
filterRuleSetIcmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetIcmpType.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetIcmpType.setDescription(' ICMP message type can be used to filter the packets ')
filterRuleSetIcmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetIcmpCode.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetIcmpCode.setDescription('ICMP message Code can be used to filter the packets')
filterRuleSetSrcPortOne = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetSrcPortOne.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetSrcPortOne.setDescription(' Source Port 1')
filterRuleSetSrcPortTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetSrcPortTwo.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetSrcPortTwo.setDescription(' Source Port 2')
filterRuleSetDestPortOne = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetDestPortOne.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetDestPortOne.setDescription(' Destination Port 1')
filterRuleSetDestPortTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetDestPortTwo.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetDestPortTwo.setDescription(' Destination Port 2')
filterRuleSetSrcRelationBetnPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("equalto", 1), ("notequalto", 2), ("lessthan", 3), ("greaterthan", 4), ("lessthanorequalto", 5), ("greaterthanorequalto", 6), ("range", 7), ("none", 8))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetSrcRelationBetnPorts.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetSrcRelationBetnPorts.setDescription(' relation between the Source port')
filterRuleSetDestRelationBetnPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("equalto", 1), ("notequalto", 2), ("lessthan", 3), ("greaterthan", 4), ("lessthanorequalto", 5), ("greaterthanorequalto", 6), ("range", 7), ("none", 8))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetDestRelationBetnPorts.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetDestRelationBetnPorts.setDescription(' relation between the Destination ports')
filterRuleSetTcpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 19), Bits().clone(namedValues=NamedValues(("fin", 0), ("syn", 1), ("rst", 2), ("psh", 3), ("ack", 4), ("urg", 5), ("estaslished", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetTcpFlags.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetTcpFlags.setDescription(' TCP flags can be used to filter the packets')
filterRuleSetLogAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 20), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetLogAction.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetLogAction.setDescription(' When a rule match occurs a logging message about the packet which the match occured the entry will be logged')
filterRuleSetConfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("insert", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetConfigure.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetConfigure.setDescription(" This variable is used to append or insert a given filter rule to the filter rule set. If 'insert' is the command the linenumber at which the rule is inserted should be available in filterRuleSetLineNumber.'If command is 'add' then the line number should contain the invalid value (OxFFFF). Incase of 'add' to know the line number at which the filter rule was added the manager should do a SNMP walk ")
filterRuleSetTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 4, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filterRuleSetTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: filterRuleSetTableRowStatus.setDescription(' Used to Add or Delete a Row in the table')
filterRuleStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5), )
if mibBuilder.loadTexts: filterRuleStatsTable.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsTable.setDescription('Filter Rule Statistics Table')
filterRuleStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: filterRuleStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsTableEntry.setDescription('An entry in the Filter Rule Statistics Table')
filterRuleStatsInBoundPermittedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsInBoundPermittedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsInBoundPermittedPkts.setDescription(' Number of InBound Permitted Packets')
filterRuleStatsInBoundDeniedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsInBoundDeniedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsInBoundDeniedPkts.setDescription(' Number of InBound Denied Packets')
filterRuleStatsInBoundUnMatchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsInBoundUnMatchedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsInBoundUnMatchedPkts.setDescription(' Number of InBound UnMatched Packets')
filterRuleStatsOutBoundPermittedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsOutBoundPermittedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsOutBoundPermittedPkts.setDescription(' Number of OutBound Permitted Packets')
filterRuleStatsOutBoundDeniedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsOutBoundDeniedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsOutBoundDeniedPkts.setDescription(' Number of OutBound Denied Packets')
filterRuleStatsOutBoundUnMatchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsOutBoundUnMatchedPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsOutBoundUnMatchedPkts.setDescription(' Number of OutBound UnMatched Packets')
filterRuleStatsNonIpInBoundPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsNonIpInBoundPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsNonIpInBoundPkts.setDescription(' Number of Non Ip InBound Packets')
filterRuleStatsNonIpOutBoundPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsNonIpOutBoundPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsNonIpOutBoundPkts.setDescription(' Number of Non Ip OutBound Packets')
filterRuleStatsBadIpInBoundPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsBadIpInBoundPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsBadIpInBoundPkts.setDescription(' Number of Bad Non Ip InBound Packets')
filterRuleStatsBadIpOutBoundPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 51, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterRuleStatsBadIpOutBoundPkts.setStatus('current')
if mibBuilder.loadTexts: filterRuleStatsBadIpOutBoundPkts.setDescription(' Number of Bad Non Ip OutBound Packets')
mibBuilder.exportSymbols("TIARA-PACKETFILTER-MIB", filterRuleStatsNonIpOutBoundPkts=filterRuleStatsNonIpOutBoundPkts, filterRuleSetDestMask=filterRuleSetDestMask, filterRuleSetAction=filterRuleSetAction, filterRuleStatsTable=filterRuleStatsTable, filterRuleStatsInBoundDeniedPkts=filterRuleStatsInBoundDeniedPkts, filterRuleSetNameIn=filterRuleSetNameIn, filterRuleStatsBadIpOutBoundPkts=filterRuleStatsBadIpOutBoundPkts, filterRuleSetTcpFlags=filterRuleSetTcpFlags, filterRuleAssignTableRowStatus=filterRuleAssignTableRowStatus, filterRuleSetTos=filterRuleSetTos, filterRuleSetTableEntry=filterRuleSetTableEntry, filterRuleSetSrcPortOne=filterRuleSetSrcPortOne, filterRuleStatsOutBoundPermittedPkts=filterRuleStatsOutBoundPermittedPkts, filterRuleSetProtocolType=filterRuleSetProtocolType, filterRuleSetDestPortOne=filterRuleSetDestPortOne, filterRuleName=filterRuleName, filterRuleSetConfigure=filterRuleSetConfigure, filterRuleStatsOutBoundUnMatchedPkts=filterRuleStatsOutBoundUnMatchedPkts, filterRuleSetSrcPortTwo=filterRuleSetSrcPortTwo, filterEntryRowStatus=filterEntryRowStatus, filterNameIndexTable=filterNameIndexTable, filterRuleSetLogAction=filterRuleSetLogAction, filterRuleAssignTableEntry=filterRuleAssignTableEntry, filterRuleSetSrcMask=filterRuleSetSrcMask, filterRuleSetIcmpCode=filterRuleSetIcmpCode, filterRuleSetIcmpType=filterRuleSetIcmpType, filterRuleAssignTable=filterRuleAssignTable, tiaraPacketFilterMib=tiaraPacketFilterMib, filterRuleSetSrcRelationBetnPorts=filterRuleSetSrcRelationBetnPorts, filterRuleSetLineNo=filterRuleSetLineNo, filterRuleStatsNonIpInBoundPkts=filterRuleStatsNonIpInBoundPkts, filterRuleStatsBadIpInBoundPkts=filterRuleStatsBadIpInBoundPkts, filterRuleSetSrcIpAddr=filterRuleSetSrcIpAddr, filterRuleSetDestPortTwo=filterRuleSetDestPortTwo, filterRuleStatsInBoundUnMatchedPkts=filterRuleStatsInBoundUnMatchedPkts, filterNameIndex=filterNameIndex, filterRuleSetTable=filterRuleSetTable, filterNameIndexEntry=filterNameIndexEntry, filterRuleStatsOutBoundDeniedPkts=filterRuleStatsOutBoundDeniedPkts, filterRuleSetPrecedence=filterRuleSetPrecedence, filterRuleStatsInBoundPermittedPkts=filterRuleStatsInBoundPermittedPkts, filterRuleSetTableRowStatus=filterRuleSetTableRowStatus, filterRuleSetNameOut=filterRuleSetNameOut, filterRuleClearCounters=filterRuleClearCounters, filterRuleSetDestIpAddr=filterRuleSetDestIpAddr, filterRuleSetDestRelationBetnPorts=filterRuleSetDestRelationBetnPorts, filterEntryName=filterEntryName, PYSNMP_MODULE_ID=tiaraPacketFilterMib, filterRuleStatsTableEntry=filterRuleStatsTableEntry)