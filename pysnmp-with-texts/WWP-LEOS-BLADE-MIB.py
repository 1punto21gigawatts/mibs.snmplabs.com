#
# PySNMP MIB module WWP-LEOS-BLADE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-BLADE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Bits, IpAddress, iso, ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, Unsigned32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Bits", "IpAddress", "iso", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
RowStatus, DateAndTime, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "DisplayString", "TextualConvention", "MacAddress")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosBladeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1))
wwpLeosBladeMIB.setRevisions(('2011-10-19 00:00', '2002-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLeosBladeMIB.setRevisionsDescriptions(('The MIB module defines the managed objects for the blades available on the WWP specific products.', 'Initial creation.',))
if mibBuilder.loadTexts: wwpLeosBladeMIB.setLastUpdated('201110190000Z')
if mibBuilder.loadTexts: wwpLeosBladeMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: wwpLeosBladeMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwpLeosBladeMIB.setDescription('Added new last reset reasons.')
wwpLeosBladeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1))
wwpLeosBlade = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1))
wwpLeosBladeMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2))
wwpLeosBladeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0))
wwpLeosBladeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3))
wwpLeosBladeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3, 1))
wwpLeosBladeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3, 2))
wwpLeosBladeTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1), )
if mibBuilder.loadTexts: wwpLeosBladeTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeTable.setDescription('The (conceptual) table listing the Blades configured/detected.')
wwpLeosBladeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1), ).setIndexNames((0, "WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"))
if mibBuilder.loadTexts: wwpLeosBladeEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeEntry.setDescription('An entry (conceptual row) in the wwpLeosBladeTable.')
wwpLeosBladeId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosBladeId.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeId.setDescription('The object indicates the unique id for the blade.')
wwpLeosBladeType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("control", 1), ("io", 2), ("fabric", 3), ("single", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosBladeType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeType.setDescription('The object indicates whether this is a control blade, a line blade or an uplink blade.')
wwpLeosBladeCapFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosBladeCapFilename.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeCapFilename.setDescription('The capability file name (including the path, if applicable) to be read from. This is the file describing capabilities of the blade and is required to configure un unequipped blade or to add a new blade. Length of filename string must not exceed 255 alpha-numeric characters, no spaces in filenames.')
wwpLeosBladeAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosBladeAdminState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeAdminState.setDescription('The object indicates the desired state of the blade. The administrative state for control blades can be set to disabled only if the control blade has a functioning backup.')
wwpLeosBladeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("enabled", 2), ("disabled", 3), ("faulted", 4), ("unequipped", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosBladeOperState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeOperState.setDescription("The object indicates the operational state of the blade. If the blade is detected and the administrative state for that blade is enabled, then the operational state of the blade is 'enabled'. If the blade is detected, but the administrative state is 'disabled', then the operational state is also 'disabled'. A faulted state occurs when a fault or communication failure is detected on a that is in either the 'enabled' or 'disabled' operation state. Any time a blade is removed, then the blade state transitions to 'unequipped'. If a new blade replaces that blade state then the state is determined by its administrative state once it is detected ('enabled' or 'disabled').")
wwpLeosBladeStartMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosBladeStartMacAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeStartMacAddr.setDescription('Base MAC address for the Blade, from which the mac addresses for the ports on this blade are derived.')
wwpLeosBladeNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosBladeNumPorts.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeNumPorts.setDescription('The total number of physical ports present on this Blade.')
wwpLeosBladeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosBladeStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'. Object in the entry cannot be modified once the wwpLeosBladeStatus is set to 'active'.")
wwpLeosPhyBladeTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2), )
if mibBuilder.loadTexts: wwpLeosPhyBladeTable.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeTable.setDescription('The (conceptual) table listing the Blades detected(physically present).')
wwpLeosPhyBladeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1), ).setIndexNames((0, "WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"))
if mibBuilder.loadTexts: wwpLeosPhyBladeEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeEntry.setDescription('An entry (conceptual row) in the wwpLeosPhyBladeTable.')
wwpLeosPhyBladeSysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeSysUpTime.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeSysUpTime.setDescription('The time (in hundredths of a second) since the blade was last re-initialized.')
wwpLeosPhyBladeSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeSerialNum.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeSerialNum.setDescription('Serial number of the blade, represented as a string.')
wwpLeosPhyBladeBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeBoardRevision.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeBoardRevision.setDescription('Module board hardware revision represented as a string.')
wwpLeosPhyBladePostResults = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladePostResults.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladePostResults.setDescription('The test result string generated by the POST tests for the blade.')
wwpLeosPhyBladePostCode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladePostCode.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladePostCode.setDescription('The result code returned by the device POST test.')
wwpLeosPhyBladeMfgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeMfgDate.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeMfgDate.setDescription('The date that the blade was manufactured.')
wwpLeosPhyBladeBoardDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeBoardDesc.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeBoardDesc.setDescription('Board Description for the blade.')
wwpLeosPhyBladeNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeNumResets.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeNumResets.setDescription('This object defines the number of times that the blade has been restarted.')
wwpLeosPhyBladeLastRebootReason = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("snmp", 2), ("pwrFail", 3), ("appLoad", 4), ("errorHandler", 5), ("watchdog", 6), ("upgrade", 7), ("cli", 8), ("resetButton", 9), ("serviceModeChange", 10), ("guardianReboot", 11), ("guardianSaosRestart", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPhyBladeLastRebootReason.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeLastRebootReason.setDescription('Indicates the reason for the last reboot.')
wwpLeosPhyBladeRebootOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("reboot", 2), ("rebootReinit", 3), ("rebootCustReinit", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPhyBladeRebootOperation.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPhyBladeRebootOperation.setDescription("Writing one of the specified values to this field causes the specified type of reboot to occur. none is the value returned when this leaf is queried. writing this value to the leaf will have no effect. 'reboot' option causes the system to reboot and restart using its current configuration. 'rebootReinit' option causes the module to erase all user configuration data and reset to factory default settings. 'rebootCustReinit' option causes the module to replace the current configuration with a customer supplied default, then reboot.")
wwpLeosBladeStateChange = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0, 1)).setObjects(("WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"), ("WWP-LEOS-BLADE-MIB", "wwpLeosBladeOperState"))
if mibBuilder.loadTexts: wwpLeosBladeStateChange.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladeStateChange.setDescription('A wwpLeosPhyBladeUpDown notification is sent whenever the operational state of the blade is changed.')
wwpLeosBladePostFail = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0, 2)).setObjects(("WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"), ("WWP-LEOS-BLADE-MIB", "wwpLeosPhyBladePostCode"))
if mibBuilder.loadTexts: wwpLeosBladePostFail.setStatus('current')
if mibBuilder.loadTexts: wwpLeosBladePostFail.setDescription('A wwpLeosBladePostFail notification is sent if the blade post tests are failed.')
mibBuilder.exportSymbols("WWP-LEOS-BLADE-MIB", wwpLeosBladeOperState=wwpLeosBladeOperState, wwpLeosPhyBladeTable=wwpLeosPhyBladeTable, wwpLeosPhyBladePostResults=wwpLeosPhyBladePostResults, wwpLeosPhyBladeEntry=wwpLeosPhyBladeEntry, wwpLeosPhyBladeSerialNum=wwpLeosPhyBladeSerialNum, wwpLeosPhyBladeBoardRevision=wwpLeosPhyBladeBoardRevision, wwpLeosBladeMIB=wwpLeosBladeMIB, wwpLeosPhyBladeBoardDesc=wwpLeosPhyBladeBoardDesc, wwpLeosBladeId=wwpLeosBladeId, wwpLeosBladeStatus=wwpLeosBladeStatus, wwpLeosBladeTable=wwpLeosBladeTable, wwpLeosPhyBladeSysUpTime=wwpLeosPhyBladeSysUpTime, wwpLeosBladeCapFilename=wwpLeosBladeCapFilename, wwpLeosBladeMIBObjects=wwpLeosBladeMIBObjects, wwpLeosPhyBladePostCode=wwpLeosPhyBladePostCode, wwpLeosBladePostFail=wwpLeosBladePostFail, wwpLeosBlade=wwpLeosBlade, wwpLeosBladeMIBConformance=wwpLeosBladeMIBConformance, wwpLeosBladeType=wwpLeosBladeType, wwpLeosPhyBladeMfgDate=wwpLeosPhyBladeMfgDate, wwpLeosPhyBladeNumResets=wwpLeosPhyBladeNumResets, wwpLeosBladeMIBNotifications=wwpLeosBladeMIBNotifications, wwpLeosBladeAdminState=wwpLeosBladeAdminState, wwpLeosBladeMIBCompliances=wwpLeosBladeMIBCompliances, wwpLeosPhyBladeRebootOperation=wwpLeosPhyBladeRebootOperation, wwpLeosBladeEntry=wwpLeosBladeEntry, wwpLeosBladeMIBGroups=wwpLeosBladeMIBGroups, wwpLeosBladeStateChange=wwpLeosBladeStateChange, wwpLeosBladeNumPorts=wwpLeosBladeNumPorts, wwpLeosBladeMIBNotificationPrefix=wwpLeosBladeMIBNotificationPrefix, wwpLeosPhyBladeLastRebootReason=wwpLeosPhyBladeLastRebootReason, PYSNMP_MODULE_ID=wwpLeosBladeMIB, wwpLeosBladeStartMacAddr=wwpLeosBladeStartMacAddr)
