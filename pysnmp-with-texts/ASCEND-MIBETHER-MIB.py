#
# PySNMP MIB module ASCEND-MIBETHER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBETHER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, MibIdentifier, Counter32, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibethernetInterfaceProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 76))
mibethernetInterfaceProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 76, 1), )
if mibBuilder.loadTexts: mibethernetInterfaceProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibethernetInterfaceProfileTable.setDescription('A list of mibethernetInterfaceProfile profile entries.')
mibethernetInterfaceProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1), ).setIndexNames((0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Shelf-o"), (0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Slot-o"), (0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Item-o"))
if mibBuilder.loadTexts: mibethernetInterfaceProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibethernetInterfaceProfileEntry.setDescription('A mibethernetInterfaceProfile entry containing objects that maps to the parameters of mibethernetInterfaceProfile profile.')
ethernetInterfaceProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 1), Integer32()).setLabel("ethernetInterfaceProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Shelf_o.setDescription('')
ethernetInterfaceProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 2), Integer32()).setLabel("ethernetInterfaceProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Slot_o.setDescription('')
ethernetInterfaceProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 3), Integer32()).setLabel("ethernetInterfaceProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Item_o.setDescription('')
ethernetInterfaceProfile_InterfaceAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("ethernetInterfaceProfile-InterfaceAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
ethernetInterfaceProfile_InterfaceAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ethernetInterfaceProfile-InterfaceAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
ethernetInterfaceProfile_InterfaceAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 6), Integer32()).setLabel("ethernetInterfaceProfile-InterfaceAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_InterfaceAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
ethernetInterfaceProfile_LinkStateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-LinkStateEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_LinkStateEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_LinkStateEnabled.setDescription('TRUE if the link state is honored, otherwise FALSE.')
ethernetInterfaceProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Enabled.setDescription('TRUE if the interface is enabled, otherwise FALSE.')
ethernetInterfaceProfile_EtherIfType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aui", 1), ("coax", 2), ("utp", 3)))).setLabel("ethernetInterfaceProfile-EtherIfType").setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetInterfaceProfile_EtherIfType.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_EtherIfType.setDescription('The type of phyical interrface, UTP, COAX, AUI')
ethernetInterfaceProfile_Filter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 10), Integer32()).setLabel("ethernetInterfaceProfile-Filter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Filter.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Filter.setDescription('This field is for non-tnt only')
ethernetInterfaceProfile_BridgingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-BridgingEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingEnabled.setDescription('TRUE if this interface is to support bridging.')
ethernetInterfaceProfile_FilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 12), DisplayString()).setLabel("ethernetInterfaceProfile-FilterName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_FilterName.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_FilterName.setDescription('The name of this filter. All filters are referenced by name so a name must be assigned to active filters.')
ethernetInterfaceProfile_DuplexMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullDuplex", 1), ("halfDuplex", 2)))).setLabel("ethernetInterfaceProfile-DuplexMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_DuplexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_DuplexMode.setDescription('Set the 100BaseT physical interface to full or half duplex mode. Only valid for the 100BaseT port.')
ethernetInterfaceProfile_PppoeOptions_Pppoe = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-PppoeOptions-Pppoe").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_PppoeOptions_Pppoe.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_PppoeOptions_Pppoe.setDescription('Enable or disable the ability to establish PPP over Ethernet session over this interface.')
ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-PppoeOptions-BridgeNonPppoe").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe.setDescription('States wheather to bridge all other protocols except PPPoE on this interface or not.')
ethernetInterfaceProfile_BridgingOptions_BridgingGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 16), Integer32()).setLabel("ethernetInterfaceProfile-BridgingOptions-BridgingGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_BridgingGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_BridgingGroup.setDescription('Select the bridging group for this connection. Group 0 disables bridging. All packets not routed will be bridged to interfaces belonging to the same group.')
ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-BridgingOptions-DialOnBroadcast").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast.setDescription('Enable/disable outdial when broadcast frames are received.')
ethernetInterfaceProfile_BridgingOptions_IpxSpoofing = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("clientSpoofing", 2), ("serverSpoofing", 3)))).setLabel("ethernetInterfaceProfile-BridgingOptions-IpxSpoofing").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_IpxSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_IpxSpoofing.setDescription('Selects the IPX spoofing mode when bridging.')
ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 19), Integer32()).setLabel("ethernetInterfaceProfile-BridgingOptions-SpoofingTimeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout.setDescription('IPX NetWare connection timeout value.')
ethernetInterfaceProfile_BridgingOptions_Fill2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 20), Integer32()).setLabel("ethernetInterfaceProfile-BridgingOptions-Fill2").setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_Fill2.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_Fill2.setDescription('filler to get to 32 bit boundary')
ethernetInterfaceProfile_BridgingOptions_BridgeType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transparentBridging", 1), ("ipxClientBridging", 2), ("noBridging", 3)))).setLabel("ethernetInterfaceProfile-BridgingOptions-BridgeType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_BridgeType.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_BridgeType.setDescription('For the P25 user interface.')
ethernetInterfaceProfile_BridgingOptions_Egress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-BridgingOptions-Egress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_Egress.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_BridgingOptions_Egress.setDescription('Enable/disable Egress on this interface. This interface will become the exit path for all packets destined to the network.')
ethernetInterfaceProfile_MediaSpeedMbit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("n-10mb", 1), ("n-100mb", 2)))).setLabel("ethernetInterfaceProfile-MediaSpeedMbit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_MediaSpeedMbit.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_MediaSpeedMbit.setDescription('Set the BaseT physical interface media speed to 100mb or 10mb. Only valid for the BaseT port on an ether3-card.')
ethernetInterfaceProfile_AutoNegotiate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ethernetInterfaceProfile-AutoNegotiate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_AutoNegotiate.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_AutoNegotiate.setDescription('Set the auto-negotiation option. Only valid for enet3nd-card.')
ethernetInterfaceProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ethernetInterfaceProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterfaceProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ethernetInterfaceProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBETHER-MIB", ethernetInterfaceProfile_InterfaceAddress_ItemNumber=ethernetInterfaceProfile_InterfaceAddress_ItemNumber, mibethernetInterfaceProfileEntry=mibethernetInterfaceProfileEntry, ethernetInterfaceProfile_BridgingOptions_Egress=ethernetInterfaceProfile_BridgingOptions_Egress, ethernetInterfaceProfile_BridgingOptions_IpxSpoofing=ethernetInterfaceProfile_BridgingOptions_IpxSpoofing, ethernetInterfaceProfile_Filter=ethernetInterfaceProfile_Filter, ethernetInterfaceProfile_Action_o=ethernetInterfaceProfile_Action_o, ethernetInterfaceProfile_BridgingOptions_BridgeType=ethernetInterfaceProfile_BridgingOptions_BridgeType, ethernetInterfaceProfile_BridgingEnabled=ethernetInterfaceProfile_BridgingEnabled, mibethernetInterfaceProfileTable=mibethernetInterfaceProfileTable, ethernetInterfaceProfile_Slot_o=ethernetInterfaceProfile_Slot_o, mibethernetInterfaceProfile=mibethernetInterfaceProfile, ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast=ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast, ethernetInterfaceProfile_Shelf_o=ethernetInterfaceProfile_Shelf_o, ethernetInterfaceProfile_DuplexMode=ethernetInterfaceProfile_DuplexMode, ethernetInterfaceProfile_AutoNegotiate=ethernetInterfaceProfile_AutoNegotiate, ethernetInterfaceProfile_BridgingOptions_Fill2=ethernetInterfaceProfile_BridgingOptions_Fill2, ethernetInterfaceProfile_Item_o=ethernetInterfaceProfile_Item_o, ethernetInterfaceProfile_LinkStateEnabled=ethernetInterfaceProfile_LinkStateEnabled, ethernetInterfaceProfile_MediaSpeedMbit=ethernetInterfaceProfile_MediaSpeedMbit, ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout=ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout, ethernetInterfaceProfile_PppoeOptions_Pppoe=ethernetInterfaceProfile_PppoeOptions_Pppoe, ethernetInterfaceProfile_FilterName=ethernetInterfaceProfile_FilterName, ethernetInterfaceProfile_Enabled=ethernetInterfaceProfile_Enabled, ethernetInterfaceProfile_EtherIfType=ethernetInterfaceProfile_EtherIfType, DisplayString=DisplayString, ethernetInterfaceProfile_InterfaceAddress_Slot=ethernetInterfaceProfile_InterfaceAddress_Slot, ethernetInterfaceProfile_BridgingOptions_BridgingGroup=ethernetInterfaceProfile_BridgingOptions_BridgingGroup, ethernetInterfaceProfile_InterfaceAddress_Shelf=ethernetInterfaceProfile_InterfaceAddress_Shelf, ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe=ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe)