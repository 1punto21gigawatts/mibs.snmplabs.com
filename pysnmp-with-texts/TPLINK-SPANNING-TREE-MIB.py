#
# PySNMP MIB module TPLINK-SPANNING-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SPANNING-TREE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, MibIdentifier, ObjectIdentity, Unsigned32, IpAddress, iso, ModuleIdentity, NotificationType, Counter32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkSpanningTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 21))
tplinkSpanningTreeMIB.setRevisions(('2012-11-21 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setLastUpdated('201211210930Z')
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setDescription('Private MIB for Spanning-Tree.')
tplinkSpanningTreeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1))
tpStpBasicCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1))
tpStpBasicGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1))
tpStpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpEnable.setDescription('Spanning Tree Protocol. 0. disable 1. enable')
tpRstpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRstpEnable.setStatus('current')
if mibBuilder.loadTexts: tpRstpEnable.setDescription('Rapid Spanning Tree Protocol. 0. disable 1. enable')
tpMstpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpEnable.setStatus('current')
if mibBuilder.loadTexts: tpMstpEnable.setDescription('Multiple Spanning Tree Protocol. 0. disable 1. enable')
tpStpBasicParamConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2))
tpStpCistPriority = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpCistPriority.setStatus('current')
if mibBuilder.loadTexts: tpStpCistPriority.setDescription('Enter a value from 0 to 61440 to specify the priority of the switch for comparison in the CIST. CIST priority is an important criterion on determining the root bridge. In the same condition, the switch with the highest priority will be chosen as the root bridge. The lower value has the higher priority. The value could be devided exactly by 4096.')
tpStpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpHelloTime.setStatus('current')
if mibBuilder.loadTexts: tpStpHelloTime.setDescription('Enter a value from 1 to 10 in seconds to specify the interval to send BPDU packets. It is used to test the links. (tpStpHelloTime+1)*2<=tpStpAgingTime.')
tpStpAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpAgingTime.setStatus('current')
if mibBuilder.loadTexts: tpStpAgingTime.setDescription('Enter a value from 6 to 40 in seconds to specify the maximum time the switch can wait without receiving a BPDU before attempting to reconfigure. (tpStpHelloTime+1)*2<=tpStpAgingTime.')
tpStpForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpForwardDelay.setStatus('current')
if mibBuilder.loadTexts: tpStpForwardDelay.setDescription('Enter a value from 4 to 30 in seconds to specify the time for the port to transit its state after the network topology is changed. stpAgingTime<=(stpForwardDelay-1)*2.')
tpStpHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpHoldCount.setStatus('current')
if mibBuilder.loadTexts: tpStpHoldCount.setDescription('Enter a value from 1 to 20 to set the maximum number of BPDU packets transmitted per Hello Time interval.')
tpStpMaxHops = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpMaxHops.setStatus('current')
if mibBuilder.loadTexts: tpStpMaxHops.setDescription('Enter a value from 1 to 40 to set the maximum number of hops that occur in a specific region before the BPDU is discarded.')
tpStpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3))
tpStpEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpEnableStatus.setStatus('current')
if mibBuilder.loadTexts: tpStpEnableStatus.setDescription('0. disable 1. enable')
tpStpMode = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stp", 1), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpMode.setStatus('current')
if mibBuilder.loadTexts: tpStpMode.setDescription('1. stp 2. rstp 3. mstp')
tpStpLocalBridge = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpLocalBridge.setStatus('current')
if mibBuilder.loadTexts: tpStpLocalBridge.setDescription('Local bridge.')
tpStpCISTRoot = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpCISTRoot.setStatus('current')
if mibBuilder.loadTexts: tpStpCISTRoot.setDescription('CIST Root.')
tpStpExPathCost = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpExPathCost.setStatus('current')
if mibBuilder.loadTexts: tpStpExPathCost.setDescription('External Path cost.')
tpStpRegionRoot = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpRegionRoot.setStatus('current')
if mibBuilder.loadTexts: tpStpRegionRoot.setDescription('Region Root.')
tpStpInPathCost = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpInPathCost.setStatus('current')
if mibBuilder.loadTexts: tpStpInPathCost.setDescription('Internal Path cost.')
tpStpDesignatedBridge = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDesignatedBridge.setStatus('current')
if mibBuilder.loadTexts: tpStpDesignatedBridge.setDescription('Designated Bridge.')
tpStpRootPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpRootPort.setStatus('current')
if mibBuilder.loadTexts: tpStpRootPort.setDescription('RootPort.')
tpStpLastTopologyChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpLastTopologyChangeTime.setStatus('current')
if mibBuilder.loadTexts: tpStpLastTopologyChangeTime.setDescription('LastTopologyChangeTime.')
tpStpTopologyChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpTopologyChangeCounter.setStatus('current')
if mibBuilder.loadTexts: tpStpTopologyChangeCounter.setDescription('TopologyChangeCounter.')
tpStpPortCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2))
tpStpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1), )
if mibBuilder.loadTexts: tpStpPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpStpPortConfigTable.setDescription('Here you can configure the parameters of the ports for comparison in the CIST and the common parameters of all Instances. And you can view the status of the ports in the CIST. CIST (Common and Internal Spanning Tree) is the spanning tree in a switched network, connecting all devices in the network.')
tpStpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpStpPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpStpPortConfigEntry.setDescription('An entry contains of the information of a port.')
tpStpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortNumber.setStatus('current')
if mibBuilder.loadTexts: tpStpPortNumber.setDescription('Displays the port number of the switch.')
tpStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1), ("errPort", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpPortEnable.setDescription('Select Enable /Disable STP function for the desired port. 0. Disable 1. Enable 2. ErrPort')
tpStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortPriority.setStatus('current')
if mibBuilder.loadTexts: tpStpPortPriority.setDescription('Enter a value from 0 to 240 divisible by 16. Port priority is an important criterion on determining the root port. In the same condition, the port with the highest priority will be chosen as the root port. The lower value has the higher priority.')
tpStpPortExPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortExPathCost.setStatus('current')
if mibBuilder.loadTexts: tpStpPortExPathCost.setDescription('ExPath Cost is used to choose the path and calculate the path costs of ports in different MST regions. It is an important criterion on determining the root port. The lower value has the higher priority. automatic when value is zero. Make sure that Path Cost ranges from 0 to 2000000.')
tpStpPortInPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortInPathCost.setStatus('current')
if mibBuilder.loadTexts: tpStpPortInPathCost.setDescription('InPath Cost is used to choose the path and calculate the path costs of ports in an MST region. It is an important criterion on determining the root port. The lower value has the higher priority. Make sure that Path Cost ranges from 0 to 2000000.')
tpStpEdgePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpEdgePortStatus.setStatus('current')
if mibBuilder.loadTexts: tpStpEdgePortStatus.setDescription('Select Enable/Disable Edge Port. The edge port can transit its state from blocking to forwarding rapidly without waiting for forward delay. 0. Disable 1. Enable')
tpStpPointToPointStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("force-enable", 1), ("force-disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPointToPointStatus.setStatus('current')
if mibBuilder.loadTexts: tpStpPointToPointStatus.setDescription('Select the P2P link status. If the two ports in the P2P link are root port or designated port, they can transit their states to forwarding rapidly to reduce the unnecessary forward delay. 0. auto 1. force enable 2. force disable')
tpStpPortMCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unChange", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortMCheck.setStatus('current')
if mibBuilder.loadTexts: tpStpPortMCheck.setDescription('Select Enable to perform MCheck operation on the port. Unchange means no MCheck operation. 0. unChange 1. enable')
tpStpPortStpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("n-a", 0), ("stp", 1), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortStpVersion.setStatus('current')
if mibBuilder.loadTexts: tpStpPortStpVersion.setDescription('Displays the STP version of the port. 1. stp 2. rstp 3. mstp')
tpStpPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("alternate", 2), ("backup", 3), ("designated", 4), ("root", 5), ("master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortRole.setStatus('current')
if mibBuilder.loadTexts: tpStpPortRole.setDescription('Displays the role of the port played in the STP Instance. 1.Disable:Indicates the port that is not participating in the STP. 2.Alternate:Indicates the port that can be a backup port of a root or master port. 3.Backup:Indicates the port that is the backup port of a designated port. 4.Designated:Indicates the port that forwards packets to a downstream network segment or switch. 5.root:Indicates the port that has the lowest path cost from this bridge to the Root Bridge and forwards packets to the root. 6.Master:Indicates the port that connects a MST region to the common root. The path from the master port to the common root is the shortest path between this MST region and the common root.')
tpStpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("n-a", 0), ("disconnected", 1), ("blocking", 2), ("learning", 3), ("forwarding", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortStatus.setStatus('current')
if mibBuilder.loadTexts: tpStpPortStatus.setDescription('Displays the working status of the port. 1.Disconnected: In this status the port is not participating in the STP. 2.Blocking: In this status the port can only receive BPDU packets. 3.Learning: In this status the port can receive/send BPDU packets and learn MAC address. 4.Forwarding: In this status the port can receive/forward data, receive/send BPDU packets as well as learn MAC address. ')
tpStpPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortLag.setStatus('current')
if mibBuilder.loadTexts: tpStpPortLag.setDescription('Displays the LAG number which the port belongs to.')
tpStpInstanceCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3))
tpMstpRegionConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1))
tpMstpRegionName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpRegionName.setStatus('current')
if mibBuilder.loadTexts: tpMstpRegionName.setDescription('Create a name for MST region identification using up to 32 characters.')
tpMstpRevision = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpRevision.setStatus('current')
if mibBuilder.loadTexts: tpMstpRevision.setDescription('Enter the revision from 0 to 65535 for MST region identification.')
tpMstpInstanceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2), )
if mibBuilder.loadTexts: tpMstpInstanceConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstanceConfigTable.setDescription('Here you can set the VLAN-to-spanning-tree mapping configuration.')
tpMstpInstanceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1), ).setIndexNames((0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstanceId"))
if mibBuilder.loadTexts: tpMstpInstanceConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstanceConfigEntry.setDescription('An entry contains of the mstp instance.')
tpMstpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstanceId.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstanceId.setDescription('Displays Instance ID of the switch,0 representative CIST. ')
tpMstpInstanceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstanceEnable.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstanceEnable.setDescription('Displays status of the instance. 0. Disable 1. Enable')
tpMstpInstancePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePriority.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePriority.setDescription('Enter the priority of the switch in the instance. It is an important criterion on determining if the switch will be chosen as the root bridge in the specific instance.Make sure that Priority ranges from 0 to 61440 and could be divided exactly by 4096')
tpMstpInstanceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstanceVlanId.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstanceVlanId.setDescription("Enter the desired VLAN ID. After modification here, the new VLAN ID will be added to the corresponding instance ID and the previous VLAN ID won't be replaced.The format of input VLAN ID shoud be like '1,3,4-7,11-30' in the range from 1 to 4094.")
tpMstpClearInstanceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpClearInstanceVlanId.setStatus('current')
if mibBuilder.loadTexts: tpMstpClearInstanceVlanId.setDescription("This object use to clear instance's vlan id.The cleared VLAN ID will be automatically mapped to the CIST.")
tpMstpInstancePortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3), )
if mibBuilder.loadTexts: tpMstpInstancePortConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortConfigTable.setDescription('A port can play different roles in different spanning tree instance. Here you can configure the parameters of the ports in different instance IDs as well as view status of the ports in the specified instance. ')
tpMstpInstancePortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1), ).setIndexNames((0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstancePortConfigId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpMstpInstancePortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortConfigEntry.setDescription('An entry contains of the mstp instance port config.')
tpMstpInstancePortConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortConfigId.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortConfigId.setDescription('The instance ID for its port configuration, 1-8.')
tpMstpInstancePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortNumber.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortNumber.setDescription('Displays the port number of the switch.')
tpMstpInstancePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePortPriority.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortPriority.setDescription('Enter the priority of the port in the instance. It is an important criterion on determining if the port will be chosen as the root port by the device connected to this port.')
tpMstpInstancePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePortPathCost.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortPathCost.setDescription('Path Cost is used to choose the path and calculate the path costs of ports in an MST region. It is an important criterion on determining the root port. The lower value has the higher priority.')
tpMstpInstancePortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("alternate", 2), ("backup", 3), ("designated", 4), ("root", 5), ("master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortRole.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortRole.setDescription('Displays the role of the port played in the STP Instance. 1. Disable 2. Alternate 3. Backup 4. Designated 5. root 6. Master')
tpMstpInstancePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("blocking", 2), ("learning", 3), ("forwarding", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortStatus.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortStatus.setDescription('Displays the working status of the port. 1. Disable 2. Blocking 3. Learning 4. Forwarding')
tpMstpInstancePortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortLag.setStatus('current')
if mibBuilder.loadTexts: tpMstpInstancePortLag.setDescription('Displays the LAG number which the port belongs to.')
tpStpSecurityCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4))
tpStpPortDefendTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1), )
if mibBuilder.loadTexts: tpStpPortDefendTable.setStatus('current')
if mibBuilder.loadTexts: tpStpPortDefendTable.setDescription('Port defend function is to prevent the devices from any malicious attack against STP features..')
tpStpPortDefendEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpStpPortDefendEntry.setStatus('current')
if mibBuilder.loadTexts: tpStpPortDefendEntry.setDescription('An entry contains of the information of a port protection.')
tpStpDefendPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDefendPortNumber.setStatus('current')
if mibBuilder.loadTexts: tpStpDefendPortNumber.setDescription('Displays the port number of the switch.')
tpStpLoopDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpLoopDefendEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpLoopDefendEnable.setDescription('Loop defend is to prevent the loops in the network brought by recalculating STP because of link failures and network congestions. 0. Disable 1. Enable')
tpStpRootBridgeDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpRootBridgeDefendEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpRootBridgeDefendEnable.setDescription('Root defend is to prevent wrong network topology change caused by the role change of the current legal root bridge. 0. Disable 1. Enable')
tpStpTcDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpTcDefendEnable.setDescription('TC defend is to prevent the decrease of the performance and stability of the switch brought by continuously removing MAC address entries upon receiving TC-BPDUs in the STP network. 0. Disable 1. Enable')
tpStpBPDUDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpBPDUDefendEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpBPDUDefendEnable.setDescription('BPDU defend is to prevent BPDUs flood in the STP network. 0. Disable 1. Enable')
tpStpBPDUHoldEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpBPDUHoldEnable.setStatus('current')
if mibBuilder.loadTexts: tpStpBPDUHoldEnable.setDescription('0. Disable 1. Enable')
tpStpDefendPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDefendPortLag.setStatus('current')
if mibBuilder.loadTexts: tpStpDefendPortLag.setDescription('Displays the LAG number which the port belongs to.')
tpStpTcDefendConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2))
tpStpTcDefendThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendThreshold.setStatus('current')
if mibBuilder.loadTexts: tpStpTcDefendThreshold.setDescription('Enter a number from 1 to 100. It is the maximum number of the TC-BPDUs received by the switch in a TC Protect Cycle.')
tpStpTcDefendTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendTimer.setStatus('current')
if mibBuilder.loadTexts: tpStpTcDefendTimer.setDescription('Enter a value from 1 to 10 to specify the TC Protect Cycle.')
tplinkSpanningTreeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 2))
tpMstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 21, 2, 1))
if mibBuilder.loadTexts: tpMstpTopologyChange.setStatus('current')
if mibBuilder.loadTexts: tpMstpTopologyChange.setDescription('The topology of spanning tree has changed.')
mibBuilder.exportSymbols("TPLINK-SPANNING-TREE-MIB", tpStpAgingTime=tpStpAgingTime, tpMstpInstancePortConfigEntry=tpMstpInstancePortConfigEntry, tpStpPortStatus=tpStpPortStatus, tpStpTopologyChangeCounter=tpStpTopologyChangeCounter, tpStpPortCfg=tpStpPortCfg, tpStpBasicGlobalConfig=tpStpBasicGlobalConfig, tpMstpInstancePortPathCost=tpMstpInstancePortPathCost, tpStpBasicParamConfig=tpStpBasicParamConfig, tpStpInPathCost=tpStpInPathCost, tpStpPortStpVersion=tpStpPortStpVersion, tpStpForwardDelay=tpStpForwardDelay, tpStpTcDefendTimer=tpStpTcDefendTimer, tpStpMaxHops=tpStpMaxHops, tpMstpRevision=tpMstpRevision, tpMstpInstancePortPriority=tpMstpInstancePortPriority, tplinkSpanningTreeMIBObjects=tplinkSpanningTreeMIBObjects, tpStpRootPort=tpStpRootPort, tpStpLastTopologyChangeTime=tpStpLastTopologyChangeTime, tplinkSpanningTreeNotifications=tplinkSpanningTreeNotifications, tpStpHoldCount=tpStpHoldCount, tpStpPortRole=tpStpPortRole, tpMstpTopologyChange=tpMstpTopologyChange, tpStpPortInPathCost=tpStpPortInPathCost, tpStpMode=tpStpMode, tplinkSpanningTreeMIB=tplinkSpanningTreeMIB, tpStpTcDefendThreshold=tpStpTcDefendThreshold, tpMstpInstancePortLag=tpMstpInstancePortLag, tpStpPortConfigTable=tpStpPortConfigTable, tpStpPortExPathCost=tpStpPortExPathCost, tpStpBPDUDefendEnable=tpStpBPDUDefendEnable, tpMstpInstancePortConfigId=tpMstpInstancePortConfigId, tpStpCISTRoot=tpStpCISTRoot, tpMstpInstanceEnable=tpMstpInstanceEnable, tpMstpInstancePriority=tpMstpInstancePriority, tpMstpInstancePortStatus=tpMstpInstancePortStatus, tpStpInstanceCfg=tpStpInstanceCfg, tpStpRootBridgeDefendEnable=tpStpRootBridgeDefendEnable, tpMstpClearInstanceVlanId=tpMstpClearInstanceVlanId, tpStpEdgePortStatus=tpStpEdgePortStatus, tpMstpInstancePortRole=tpMstpInstancePortRole, tpStpPortDefendEntry=tpStpPortDefendEntry, tpMstpRegionConfig=tpMstpRegionConfig, tpStpDefendPortNumber=tpStpDefendPortNumber, tpStpExPathCost=tpStpExPathCost, tpMstpInstanceVlanId=tpMstpInstanceVlanId, tpMstpInstanceConfigEntry=tpMstpInstanceConfigEntry, tpStpDefendPortLag=tpStpDefendPortLag, tpStpPortPriority=tpStpPortPriority, tpStpLocalBridge=tpStpLocalBridge, tpStpCistPriority=tpStpCistPriority, tpStpPortNumber=tpStpPortNumber, PYSNMP_MODULE_ID=tplinkSpanningTreeMIB, tpStpBPDUHoldEnable=tpStpBPDUHoldEnable, tpStpEnable=tpStpEnable, tpStpTcDefendConfig=tpStpTcDefendConfig, tpStpPortLag=tpStpPortLag, tpStpPortDefendTable=tpStpPortDefendTable, tpStpEnableStatus=tpStpEnableStatus, tpStpDesignatedBridge=tpStpDesignatedBridge, tpStpPortMCheck=tpStpPortMCheck, tpMstpEnable=tpMstpEnable, tpStpBasicCfg=tpStpBasicCfg, tpMstpRegionName=tpMstpRegionName, tpStpLoopDefendEnable=tpStpLoopDefendEnable, tpMstpInstanceConfigTable=tpMstpInstanceConfigTable, tpStpHelloTime=tpStpHelloTime, tpStpInfo=tpStpInfo, tpStpPortConfigEntry=tpStpPortConfigEntry, tpStpTcDefendEnable=tpStpTcDefendEnable, tpStpPortEnable=tpStpPortEnable, tpRstpEnable=tpRstpEnable, tpStpRegionRoot=tpStpRegionRoot, tpMstpInstanceId=tpMstpInstanceId, tpMstpInstancePortConfigTable=tpMstpInstancePortConfigTable, tpStpPointToPointStatus=tpStpPointToPointStatus, tpStpSecurityCfg=tpStpSecurityCfg, tpMstpInstancePortNumber=tpMstpInstancePortNumber)