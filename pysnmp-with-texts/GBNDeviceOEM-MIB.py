#
# PySNMP MIB module GBNDeviceOEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNDeviceOEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
gbnDevice, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnDevice")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
IpAddress, Integer32, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, Unsigned32, Counter64, Bits, NotificationType, Gauge32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
bcm5600 = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3))
bcm5600.setRevisions(('1901-05-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcm5600.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: bcm5600.setLastUpdated('0105030000Z')
if mibBuilder.loadTexts: bcm5600.setOrganization('Greentech')
if mibBuilder.loadTexts: bcm5600.setContactInfo('Adam Armstrong E-mail: adama@observium.org')
if mibBuilder.loadTexts: bcm5600.setDescription('GBN Broadcom BCM5600 StrataSwitch OEM-Product Enterprise MIB definition.')
oemArchIface = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1))
oemChip = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 2))
oemProdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3))
oemProdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1))
oemProdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 2))
oemArchIfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1), )
if mibBuilder.loadTexts: oemArchIfaceTable.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceTable.setDescription('A table of switch interfaces and associated properties.')
oemArchIfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1), ).setIndexNames((0, "GBNDeviceOEM-MIB", "oemArchIfaceUnit"), (0, "GBNDeviceOEM-MIB", "oemArchIfacePort"))
if mibBuilder.loadTexts: oemArchIfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceEntry.setDescription('Table entry for switch interface control and status information.')
oemArchIfaceUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceUnit.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceUnit.setDescription("An index that uniquely identifies a unit in the QTECH Switch stack. If an invalid value is used for the index, a SNMP 'noSuchName' error (SNMPv1) or 'noSuchInstance' exception (SNMPv2/v3) is returned. For implementations that do not support stacking, the same response is returned for any unit index other than 1.")
oemArchIfacePort = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfacePort.setStatus('current')
if mibBuilder.loadTexts: oemArchIfacePort.setDescription("An index that uniquely identifies a GBN Application 'logical port' (i.e., IEEE 802.3ad Aggregator) within the oemArchIfaceUnit.")
oemArchIfaceLLWHPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8193, 8296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceLLWHPort.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceLLWHPort.setDescription("A value that uniquely identifies a GBN Application 'logical port' (i.e., IEEE 802.3ad Aggregator) in the GBN BCM5600 stack. This is a 'Layered Linear With Holes' (LLWH) port number that may may have holes for missing ports or units. For this MIB, 26 port numbers are reserved for each unit in the stack. For example, LLHW port 8193 is unit 1, port 1 .")
oemArchIfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceIfIndex.setDescription("The ifIndex of this GBN Application 'logical port' (i.e., IEEE 802.3ad Aggregator). Note that an ifIndex value of 34603009 (0x02100001) represents the Aggregator layer, unit 1, slot 0 (base unit ports), port 1.")
oemArchIfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceName.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceName.setDescription("DURABLE: The textual name of this interface, e.g., 'John'.")
oemArchIfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceEnable.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceEnable.setDescription("DURABLE: { true:all } This object is true(1) when this interface is enabled and false(1) when it is disabled. For this product, this is the ONLY way to enable or disable this interface. Note that 'ifAdminStatus' in RFC1213 and RFC2233 and 'dot1dStpPortEnable' in RFC1493 are each implemented as 'read-only'.")
oemArchIfaceSTPEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceSTPEnable.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceSTPEnable.setDescription('DURABLE: { true:all } This object is true(1) when Spanning Tree operation is enabled for this interface and false(2) when it is disabled.')
oemArchIfaceLink = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceLink.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceLink.setDescription('The state of Link Detect on this interface.')
oemArchIfaceDuplexSpeedSet = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 99))).clone(namedValues=NamedValues(("autonegotiate", 1), ("half-10", 2), ("full-10", 3), ("half-100", 4), ("full-100", 5), ("half-1000", 6), ("full-1000", 7), ("illegal", 99)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceDuplexSpeedSet.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceDuplexSpeedSet.setDescription('DURABLE: { autonegotiate:all } The desired speed and duplex for this interface. If the selected control is not possible on the interface, a value of illegal(99) is returned. If the port type does NOT support the default of autonegotiate(1), then the application initializes the port to a valid value (e.g., 1000full(6)). Note that not all controls are possible for all interfaces. For example, only full-1000(6) is available for Gigabit Ethernet interfaces.')
oemArchIfaceDuplexSpeedGet = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99))).clone(namedValues=NamedValues(("unknown", 1), ("half-10", 2), ("full-10", 3), ("half-100", 4), ("full-100", 5), ("half-1000", 6), ("full-1000", 7), ("auto_10", 8), ("auto_100", 9), ("auto_1000", 10), ("illegal", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceDuplexSpeedGet.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceDuplexSpeedGet.setDescription("The actual speed and duplex for this interface. If the interface is not configured for an acceptable value, a value of illegal(99) is returned. A value of unknown(1) is returned when the 'oemArchIfaceLink' indicates down(2) for this interface.")
oemArchIfacePortLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internalEnable", 1), ("externalEnable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfacePortLoop.setStatus('current')
if mibBuilder.loadTexts: oemArchIfacePortLoop.setDescription('The state of Link Detect on this interface.')
oemArchIfaceFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceFlowControl.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceFlowControl.setDescription('DURABLE: { enable } Set the flow control on the interface to enable(1) or disable(2).')
oemArchIfaceTxVlanTagPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceTxVlanTagPkts.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceTxVlanTagPkts.setDescription('The number of VLAN tagged packets transmitted on this interface.')
oemArchIfaceTxL3Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceTxL3Pkts.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceTxL3Pkts.setDescription('The number of Layer 3 packets transmitted on this interface.')
oemArchIfaceTxL3AbortedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceTxL3AbortedPkts.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceTxL3AbortedPkts.setDescription('The number of Layer 3 transmit packets aborted on this interface.')
oemArchIfaceRxIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oemArchIfaceRxIpInHdrErrors.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceRxIpInHdrErrors.setDescription('The number of Layer 3 packets received on this interface that were discarded due to IP header errors (e.g., bad checksum, invalid versions, format errors).')
oemArchIfaceL2Tunneling = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemArchIfaceL2Tunneling.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceL2Tunneling.setDescription("When l2 entities (such as STP bridges) conneted across a VPN network, l2 PDUs need delivering through VPN without being processed.To achieve this, users need enbling l2- tunneling on VPN's edge ports, i.e. ports connected to customer bridges. One 32bits width integer variable is used for each port to represent what kind of PDUs need tunneling when coming in this ports.Notes, only the six least-significant bits are used here ,each bit corresponds to one protocol, following is the detail: bit0 <----> CDP bit1 <----> LACP bit2 <----> PAGP bit3 <----> STP bit4 <----> UDLD bit5 <----> VTP bit6-bit31 <--> reserved. when set one, corresponding PDU tunneling is asserted, deasserted otherwise.")
oemChipStub = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("chip-value2", 2), ("chip-value3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oemChipStub.setStatus('current')
if mibBuilder.loadTexts: oemChipStub.setDescription('This object is a place holder for the OEM Chip interface.')
oemArchIfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1, 1)).setObjects(("GBNDeviceOEM-MIB", "oemArchIfaceLLWHPort"), ("GBNDeviceOEM-MIB", "oemArchIfaceIfIndex"), ("GBNDeviceOEM-MIB", "oemArchIfaceName"), ("GBNDeviceOEM-MIB", "oemArchIfaceEnable"), ("GBNDeviceOEM-MIB", "oemArchIfaceSTPEnable"), ("GBNDeviceOEM-MIB", "oemArchIfaceLink"), ("GBNDeviceOEM-MIB", "oemArchIfaceDuplexSpeedSet"), ("GBNDeviceOEM-MIB", "oemArchIfaceDuplexSpeedGet"), ("GBNDeviceOEM-MIB", "oemArchIfacePortLoop"), ("GBNDeviceOEM-MIB", "oemArchIfaceFlowControl"), ("GBNDeviceOEM-MIB", "oemArchIfaceTxVlanTagPkts"), ("GBNDeviceOEM-MIB", "oemArchIfaceTxL3Pkts"), ("GBNDeviceOEM-MIB", "oemArchIfaceTxL3AbortedPkts"), ("GBNDeviceOEM-MIB", "oemArchIfaceRxIpInHdrErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oemArchIfaceGroup = oemArchIfaceGroup.setStatus('current')
if mibBuilder.loadTexts: oemArchIfaceGroup.setDescription('This group configures and retrieves Architecture interface specific objects.')
oemChipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 1, 2)).setObjects(("GBNDeviceOEM-MIB", "oemChipStub"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oemChipGroup = oemChipGroup.setStatus('current')
if mibBuilder.loadTexts: oemChipGroup.setDescription('This group configures OEM Chip specific objects.')
oemProdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 3, 2, 1)).setObjects(("GBNDeviceOEM-MIB", "oemArchIfaceGroup"), ("GBNDeviceOEM-MIB", "oemChipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oemProdCompliance = oemProdCompliance.setStatus('current')
if mibBuilder.loadTexts: oemProdCompliance.setDescription('The compliance statement.')
oemArchIfaceTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2))
macAddrLimitOn = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 1)).setObjects(("GBNDeviceOEM-MIB", "ifIndex"))
if mibBuilder.loadTexts: macAddrLimitOn.setStatus('current')
if mibBuilder.loadTexts: macAddrLimitOn.setDescription('Trap sent when MAC addresses number learnt no a port reachs its up-threshole')
macAddrLimitOff = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 2)).setObjects(("GBNDeviceOEM-MIB", "ifIndex"))
if mibBuilder.loadTexts: macAddrLimitOff.setStatus('current')
if mibBuilder.loadTexts: macAddrLimitOff.setDescription('.')
stormCtrlPortShutdown = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 3)).setObjects(("GBNDeviceOEM-MIB", "ifIndex"))
if mibBuilder.loadTexts: stormCtrlPortShutdown.setStatus('current')
if mibBuilder.loadTexts: stormCtrlPortShutdown.setDescription('Trap sent when port shutdown for storm on it reachs its up-threshole')
stormCtrlPortFree = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 3, 1, 2, 4)).setObjects(("GBNDeviceOEM-MIB", "ifIndex"))
if mibBuilder.loadTexts: stormCtrlPortFree.setStatus('current')
if mibBuilder.loadTexts: stormCtrlPortFree.setDescription('.')
mibBuilder.exportSymbols("GBNDeviceOEM-MIB", oemArchIfaceLink=oemArchIfaceLink, oemArchIface=oemArchIface, oemChipGroup=oemChipGroup, oemArchIfaceTxL3AbortedPkts=oemArchIfaceTxL3AbortedPkts, oemArchIfaceIfIndex=oemArchIfaceIfIndex, stormCtrlPortShutdown=stormCtrlPortShutdown, oemProdGroups=oemProdGroups, oemArchIfaceTrap=oemArchIfaceTrap, macAddrLimitOn=macAddrLimitOn, oemArchIfaceSTPEnable=oemArchIfaceSTPEnable, oemArchIfacePortLoop=oemArchIfacePortLoop, oemChipStub=oemChipStub, oemChip=oemChip, macAddrLimitOff=macAddrLimitOff, oemArchIfaceGroup=oemArchIfaceGroup, oemProdConformance=oemProdConformance, PYSNMP_MODULE_ID=bcm5600, bcm5600=bcm5600, oemArchIfaceTable=oemArchIfaceTable, oemArchIfaceTxVlanTagPkts=oemArchIfaceTxVlanTagPkts, oemArchIfacePort=oemArchIfacePort, oemArchIfaceL2Tunneling=oemArchIfaceL2Tunneling, stormCtrlPortFree=stormCtrlPortFree, oemArchIfaceLLWHPort=oemArchIfaceLLWHPort, oemProdCompliances=oemProdCompliances, oemArchIfaceFlowControl=oemArchIfaceFlowControl, oemArchIfaceName=oemArchIfaceName, oemArchIfaceRxIpInHdrErrors=oemArchIfaceRxIpInHdrErrors, oemArchIfaceDuplexSpeedGet=oemArchIfaceDuplexSpeedGet, oemArchIfaceEntry=oemArchIfaceEntry, oemProdCompliance=oemProdCompliance, oemArchIfaceUnit=oemArchIfaceUnit, oemArchIfaceDuplexSpeedSet=oemArchIfaceDuplexSpeedSet, oemArchIfaceTxL3Pkts=oemArchIfaceTxL3Pkts, oemArchIfaceEnable=oemArchIfaceEnable)