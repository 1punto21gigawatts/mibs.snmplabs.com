#
# PySNMP MIB module MY-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-MEMORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:16:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Gauge32, NotificationType, TimeTicks, IpAddress, ModuleIdentity, iso, Bits, Counter64, Counter32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Gauge32", "NotificationType", "TimeTicks", "IpAddress", "ModuleIdentity", "iso", "Bits", "Counter64", "Counter32", "MibIdentifier", "Integer32")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
myMemoryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35))
myMemoryMIB.setRevisions(('2003-10-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: myMemoryMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: myMemoryMIB.setLastUpdated('200310140000Z')
if mibBuilder.loadTexts: myMemoryMIB.setOrganization('D-Link Crop.')
if mibBuilder.loadTexts: myMemoryMIB.setContactInfo(' http://support.dlink.com')
if mibBuilder.loadTexts: myMemoryMIB.setDescription('This module defines my system mibs.')
class Percent(TextualConvention, Integer32):
    description = 'An integer that is in the range of a percent value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

myMemoryPoolMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1))
myMemoryPoolUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1), )
if mibBuilder.loadTexts: myMemoryPoolUtilizationTable.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolUtilizationTable.setDescription('A table of memory pool utilization entries. Each of the objects provides a general idea of how much of the memory pool has been used over a given period of time.')
myMemoryPoolUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1), ).setIndexNames((0, "MY-MEMORY-MIB", "myMemoryPoolIndex"))
if mibBuilder.loadTexts: myMemoryPoolUtilizationEntry.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolUtilizationEntry.setDescription('An entry in the memory pool utilization table.')
myMemoryPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolIndex.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolIndex.setDescription('An index that uniquely represents a Memory Pool.')
myMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolName.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolName.setDescription('A textual name assigned to the memory pool. This object is suitable for output to a human operator')
myMemoryPoolCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolCurrentUtilization.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolCurrentUtilization.setDescription('This is the memory pool utilization currently.')
myMemoryPoolLowestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolLowestUtilization.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolLowestUtilization.setDescription('This is the memory pool utilization when memory used least.')
myMemoryPoolLargestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolLargestUtilization.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolLargestUtilization.setDescription('This is the memory pool utilization when memory used most.')
myMemoryPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolSize.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolSize.setDescription('This is the size of physical memory .')
myMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolUsed.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolUsed.setDescription('This is the memory size that has been used.')
myMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMemoryPoolFree.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolFree.setDescription('This is the memory size that is free.')
myMemoryPoolWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 9), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMemoryPoolWarning.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolWarning.setDescription('The first warning of memory pool.')
myMemoryPoolCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 10), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMemoryPoolCritical.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolCritical.setDescription('The second warning of memory pool.')
myNodeMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2), )
if mibBuilder.loadTexts: myNodeMemoryPoolTable.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolTable.setDescription("A table of node's memory pool utilization entries. Each of the objects provides a general idea of how much of the memory pool has been used over a given period of time.")
myNodeMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1), ).setIndexNames((0, "MY-MEMORY-MIB", "myNodeMemoryPoolIndex"))
if mibBuilder.loadTexts: myNodeMemoryPoolEntry.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolEntry.setDescription("An entry in the node's memory pool utilization table.")
myNodeMemoryPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolIndex.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolIndex.setDescription("An index that uniquely represents a node's Memory Pool.")
myNodeMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolName.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolName.setDescription("A textual name assigned to the node's memory pool. This object is suitable for output to a human operator")
myNodeMemoryPoolCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolCurrentUtilization.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolCurrentUtilization.setDescription("This is the node's memory pool utilization currently.")
myNodeMemoryPoolLowestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolLowestUtilization.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolLowestUtilization.setDescription("This is the node's memory pool utilization when memory used least.")
myNodeMemoryPoolLargestUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolLargestUtilization.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolLargestUtilization.setDescription("This is the node's memory pool utilization when memory used most.")
myNodeMemoryPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolSize.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolSize.setDescription("This is the size of the node's physical memory .")
myNodeMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolUsed.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolUsed.setDescription("This is the node's memory size that has been used.")
myNodeMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeMemoryPoolFree.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolFree.setDescription("This is the node's memory size that is free.")
myNodeMemoryPoolWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 9), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeMemoryPoolWarning.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolWarning.setDescription("This is the first warning of the node's memory.")
myNodeMemoryPoolCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 10), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeMemoryPoolCritical.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolCritical.setDescription("This is the second warning of the node's memory.")
myMemoryMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2))
myMemoryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1))
myMemoryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2))
myMemoryMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1, 1)).setObjects(("MY-MEMORY-MIB", "myMemoryPoolUtilizationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myMemoryMIBCompliance = myMemoryMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: myMemoryMIBCompliance.setDescription('The compliance statement for entities which implement the My Memory MIB')
myMemoryPoolUtilizationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 1)).setObjects(("MY-MEMORY-MIB", "myMemoryPoolIndex"), ("MY-MEMORY-MIB", "myMemoryPoolName"), ("MY-MEMORY-MIB", "myMemoryPoolCurrentUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolLowestUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolLargestUtilization"), ("MY-MEMORY-MIB", "myMemoryPoolSize"), ("MY-MEMORY-MIB", "myMemoryPoolUsed"), ("MY-MEMORY-MIB", "myMemoryPoolFree"), ("MY-MEMORY-MIB", "myMemoryPoolWarning"), ("MY-MEMORY-MIB", "myMemoryPoolCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myMemoryPoolUtilizationMIBGroup = myMemoryPoolUtilizationMIBGroup.setStatus('current')
if mibBuilder.loadTexts: myMemoryPoolUtilizationMIBGroup.setDescription('A collection of objects providing memory pool utilization to a My agent.')
myNodeMemoryPoolMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 2)).setObjects(("MY-MEMORY-MIB", "myNodeMemoryPoolIndex"), ("MY-MEMORY-MIB", "myNodeMemoryPoolName"), ("MY-MEMORY-MIB", "myNodeMemoryPoolCurrentUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolLowestUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolLargestUtilization"), ("MY-MEMORY-MIB", "myNodeMemoryPoolSize"), ("MY-MEMORY-MIB", "myNodeMemoryPoolUsed"), ("MY-MEMORY-MIB", "myNodeMemoryPoolFree"), ("MY-MEMORY-MIB", "myNodeMemoryPoolWarning"), ("MY-MEMORY-MIB", "myNodeMemoryPoolCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNodeMemoryPoolMIBGroup = myNodeMemoryPoolMIBGroup.setStatus('current')
if mibBuilder.loadTexts: myNodeMemoryPoolMIBGroup.setDescription("A collection of objects providing node's memory pool utilization to a My agent.")
mibBuilder.exportSymbols("MY-MEMORY-MIB", myNodeMemoryPoolCritical=myNodeMemoryPoolCritical, myNodeMemoryPoolName=myNodeMemoryPoolName, myMemoryMIBCompliance=myMemoryMIBCompliance, PYSNMP_MODULE_ID=myMemoryMIB, myMemoryMIB=myMemoryMIB, myNodeMemoryPoolFree=myNodeMemoryPoolFree, myMemoryPoolLowestUtilization=myMemoryPoolLowestUtilization, myMemoryPoolCurrentUtilization=myMemoryPoolCurrentUtilization, myNodeMemoryPoolUsed=myNodeMemoryPoolUsed, myMemoryPoolIndex=myMemoryPoolIndex, myMemoryPoolName=myMemoryPoolName, myNodeMemoryPoolCurrentUtilization=myNodeMemoryPoolCurrentUtilization, Percent=Percent, myNodeMemoryPoolWarning=myNodeMemoryPoolWarning, myMemoryMIBGroups=myMemoryMIBGroups, myMemoryPoolUsed=myMemoryPoolUsed, myNodeMemoryPoolLargestUtilization=myNodeMemoryPoolLargestUtilization, myNodeMemoryPoolEntry=myNodeMemoryPoolEntry, myMemoryPoolUtilizationTable=myMemoryPoolUtilizationTable, myMemoryPoolMIBObjects=myMemoryPoolMIBObjects, myMemoryMIBConformance=myMemoryMIBConformance, myMemoryPoolLargestUtilization=myMemoryPoolLargestUtilization, myMemoryPoolUtilizationMIBGroup=myMemoryPoolUtilizationMIBGroup, myNodeMemoryPoolSize=myNodeMemoryPoolSize, myMemoryPoolWarning=myMemoryPoolWarning, myMemoryPoolUtilizationEntry=myMemoryPoolUtilizationEntry, myMemoryPoolSize=myMemoryPoolSize, myMemoryPoolCritical=myMemoryPoolCritical, myMemoryPoolFree=myMemoryPoolFree, myNodeMemoryPoolLowestUtilization=myNodeMemoryPoolLowestUtilization, myNodeMemoryPoolIndex=myNodeMemoryPoolIndex, myNodeMemoryPoolTable=myNodeMemoryPoolTable, myNodeMemoryPoolMIBGroup=myNodeMemoryPoolMIBGroup, myMemoryMIBCompliances=myMemoryMIBCompliances)