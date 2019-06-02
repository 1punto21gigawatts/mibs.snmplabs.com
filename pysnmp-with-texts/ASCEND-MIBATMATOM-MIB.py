#
# PySNMP MIB module ASCEND-MIBATMATOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMATOM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, MibIdentifier, iso, TimeTicks, NotificationType, ModuleIdentity, ObjectIdentity, Integer32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "MibIdentifier", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatmVclProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 39))
mibatmVplProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 38))
mibatmVclProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 39, 1), )
if mibBuilder.loadTexts: mibatmVclProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmVclProfileTable.setDescription('A list of mibatmVclProfile profile entries.')
mibatmVclProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-Shelf"), (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-Slot"), (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-ItemNumber"), (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-LogicalItem"), (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Vpi"), (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Vci"))
if mibBuilder.loadTexts: mibatmVclProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmVclProfileEntry.setDescription('A mibatmVclProfile entry containing objects that maps to the parameters of mibatmVclProfile profile.')
atmVclProfile_Id_Address_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 1), Integer32()).setLabel("atmVclProfile-Id-Address-PhysicalAddress-Shelf").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
atmVclProfile_Id_Address_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 2), Integer32()).setLabel("atmVclProfile-Id-Address-PhysicalAddress-Slot").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
atmVclProfile_Id_Address_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 3), Integer32()).setLabel("atmVclProfile-Id-Address-PhysicalAddress-ItemNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Address_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
atmVclProfile_Id_Address_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 4), Integer32()).setLabel("atmVclProfile-Id-Address-LogicalItem").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Address_LogicalItem.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Address_LogicalItem.setDescription('A number that specifies an addressable logical entity within the context of a physical address.')
atmVclProfile_Id_Vpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 5), Integer32()).setLabel("atmVclProfile-Id-Vpi").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Vpi.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Vpi.setDescription('The VPI number for this Vcl.')
atmVclProfile_Id_Vci = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 6), Integer32()).setLabel("atmVclProfile-Id-Vci").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Id_Vci.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Id_Vci.setDescription('The VCI number for this Vcl.')
atmVclProfile_RxTrafficDesc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 7), Integer32()).setLabel("atmVclProfile-RxTrafficDesc").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_RxTrafficDesc.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_RxTrafficDesc.setDescription('The ATM Traffic Descriptor index applied to the receive direction of the Vcl.')
atmVclProfile_TxTrafficDesc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 8), Integer32()).setLabel("atmVclProfile-TxTrafficDesc").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_TxTrafficDesc.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_TxTrafficDesc.setDescription('The Traffic Descriptor index applied to the transmit direction of the Vcl.')
atmVclProfile_AalType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notPresent", 1), ("aal1", 2), ("aal34", 3), ("aal5", 4), ("aalOther", 5), ("aalUnknown", 6), ("aal2", 7)))).setLabel("atmVclProfile-AalType").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_AalType.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_AalType.setDescription('The type of the ATM Adaptation Layer used by this Vcl.')
atmVclProfile_TxSduSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 10), Integer32()).setLabel("atmVclProfile-TxSduSize").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_TxSduSize.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_TxSduSize.setDescription('The maximum AAL5 CPCS SDU size in octets that is supported on the transmit direction of this VCC.')
atmVclProfile_RxSduSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 11), Integer32()).setLabel("atmVclProfile-RxSduSize").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_RxSduSize.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_RxSduSize.setDescription('The maximum AAL5 CPCS SDU size in octets that is supported on the receive direction of this VCC.')
atmVclProfile_Aal5Encaps = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("vcmuxRouted", 2), ("vcmuxBridged8023", 3), ("vcmuxBridged8025", 4), ("vcmuxBridged8026", 5), ("vcmuxLanemul8023", 6), ("vcmuxLanemul8025", 7), ("llcEncapsulation", 8), ("multiFrameRelaySscs", 9), ("otherEncapsulation", 10), ("unknownEncapsulation", 11)))).setLabel("atmVclProfile-Aal5Encaps").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_Aal5Encaps.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Aal5Encaps.setDescription('The type of data encapsulation used over AAL5 SSCS Layer.')
atmVclProfile_McastType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("p2p", 2), ("p2mproot", 3), ("p2mpleaf", 4)))).setLabel("atmVclProfile-McastType").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_McastType.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_McastType.setDescription('The connection topology type.')
atmVclProfile_CallKind = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("pvc", 2), ("svcIncoming", 3), ("svcOutgoing", 4), ("spvcInitiator", 5), ("spvcTarget", 6)))).setLabel("atmVclProfile-CallKind").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVclProfile_CallKind.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_CallKind.setDescription('The use of call control.')
atmVclProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmVclProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVclProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclProfile_Action_o.setDescription('')
mibatmVplProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 38, 1), )
if mibBuilder.loadTexts: mibatmVplProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmVplProfileTable.setDescription('A list of mibatmVplProfile profile entries.')
mibatmVplProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-Shelf"), (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-Slot"), (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-ItemNumber"), (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-LogicalItem"), (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Vpi"))
if mibBuilder.loadTexts: mibatmVplProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmVplProfileEntry.setDescription('A mibatmVplProfile entry containing objects that maps to the parameters of mibatmVplProfile profile.')
atmVplProfile_Id_Address_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 1), Integer32()).setLabel("atmVplProfile-Id-Address-PhysicalAddress-Shelf").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
atmVplProfile_Id_Address_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 2), Integer32()).setLabel("atmVplProfile-Id-Address-PhysicalAddress-Slot").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
atmVplProfile_Id_Address_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 3), Integer32()).setLabel("atmVplProfile-Id-Address-PhysicalAddress-ItemNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Id_Address_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
atmVplProfile_Id_Address_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 4), Integer32()).setLabel("atmVplProfile-Id-Address-LogicalItem").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_Id_Address_LogicalItem.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Id_Address_LogicalItem.setDescription('A number that specifies an addressable logical entity within the context of a physical address.')
atmVplProfile_Id_Vpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 5), Integer32()).setLabel("atmVplProfile-Id-Vpi").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_Id_Vpi.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Id_Vpi.setDescription('The VPI number for this Vpl.')
atmVplProfile_RxTrafficDesc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 6), Integer32()).setLabel("atmVplProfile-RxTrafficDesc").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_RxTrafficDesc.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_RxTrafficDesc.setDescription('The ATM Traffic Descriptor index applied to the receive direction of the Vpl.')
atmVplProfile_TxTrafficDesc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 7), Integer32()).setLabel("atmVplProfile-TxTrafficDesc").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_TxTrafficDesc.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_TxTrafficDesc.setDescription('The ATM Traffic Descriptor index applied to the transmit direction of the Vpl.')
atmVplProfile_McastType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("p2p", 2), ("p2mproot", 3), ("p2mpleaf", 4)))).setLabel("atmVplProfile-McastType").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_McastType.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_McastType.setDescription('The connection topology type.')
atmVplProfile_CallKind = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("pvc", 2), ("svcIncoming", 3), ("svcOutgoing", 4), ("spvcInitiator", 5), ("spvcTarget", 6)))).setLabel("atmVplProfile-CallKind").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVplProfile_CallKind.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_CallKind.setDescription('The use of call control.')
atmVplProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmVplProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVplProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmVplProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBATMATOM-MIB", mibatmVplProfile=mibatmVplProfile, atmVclProfile_Id_Address_LogicalItem=atmVclProfile_Id_Address_LogicalItem, atmVplProfile_Id_Address_PhysicalAddress_Slot=atmVplProfile_Id_Address_PhysicalAddress_Slot, atmVclProfile_RxTrafficDesc=atmVclProfile_RxTrafficDesc, atmVplProfile_RxTrafficDesc=atmVplProfile_RxTrafficDesc, atmVplProfile_Id_Address_PhysicalAddress_Shelf=atmVplProfile_Id_Address_PhysicalAddress_Shelf, atmVplProfile_Action_o=atmVplProfile_Action_o, atmVplProfile_McastType=atmVplProfile_McastType, atmVplProfile_CallKind=atmVplProfile_CallKind, DisplayString=DisplayString, atmVclProfile_Id_Address_PhysicalAddress_ItemNumber=atmVclProfile_Id_Address_PhysicalAddress_ItemNumber, atmVclProfile_CallKind=atmVclProfile_CallKind, atmVclProfile_Id_Address_PhysicalAddress_Slot=atmVclProfile_Id_Address_PhysicalAddress_Slot, atmVclProfile_TxSduSize=atmVclProfile_TxSduSize, atmVclProfile_Id_Vpi=atmVclProfile_Id_Vpi, mibatmVplProfileTable=mibatmVplProfileTable, atmVclProfile_McastType=atmVclProfile_McastType, mibatmVclProfile=mibatmVclProfile, atmVplProfile_Id_Vpi=atmVplProfile_Id_Vpi, atmVclProfile_AalType=atmVclProfile_AalType, atmVclProfile_TxTrafficDesc=atmVclProfile_TxTrafficDesc, atmVclProfile_RxSduSize=atmVclProfile_RxSduSize, atmVplProfile_TxTrafficDesc=atmVplProfile_TxTrafficDesc, atmVplProfile_Id_Address_LogicalItem=atmVplProfile_Id_Address_LogicalItem, mibatmVplProfileEntry=mibatmVplProfileEntry, mibatmVclProfileTable=mibatmVclProfileTable, atmVclProfile_Action_o=atmVclProfile_Action_o, atmVplProfile_Id_Address_PhysicalAddress_ItemNumber=atmVplProfile_Id_Address_PhysicalAddress_ItemNumber, atmVclProfile_Aal5Encaps=atmVclProfile_Aal5Encaps, atmVclProfile_Id_Address_PhysicalAddress_Shelf=atmVclProfile_Id_Address_PhysicalAddress_Shelf, mibatmVclProfileEntry=mibatmVclProfileEntry, atmVclProfile_Id_Vci=atmVclProfile_Id_Vci)