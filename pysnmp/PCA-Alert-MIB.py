#
# PySNMP MIB module PCA-Alert-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCA-Alert-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, MibIdentifier, Counter32, IpAddress, NotificationType, Integer32, NotificationType, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "NotificationType", "Integer32", "NotificationType", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symantec = MibIdentifier((1, 3, 6, 1, 4, 1, 393))
pcanywhere = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100))
pcaversionnine = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9))
pcaHost = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 1))
pcaRemote = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 2))
pcaFileXfer = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 3))
pcaGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 4))
pcaMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 5))
pcaInstall = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 6))
pcaReset = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 7))
pcaLDAP = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 8))
pcaObject = MibIdentifier((1, 3, 6, 1, 4, 1, 393, 100, 9, 9))
hostComputerName = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostComputerName.setStatus('optional')
remoteComputerName = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteComputerName.setStatus('optional')
callerName = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callerName.setStatus('optional')
hostConnectionObject = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostConnectionObject.setStatus('optional')
remoteConnectionObject = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteConnectionObject.setStatus('optional')
xferFiles = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferFiles.setStatus('optional')
xferBytes = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferBytes.setStatus('optional')
xferOperation = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferOperation.setStatus('optional')
xferVirusFlag = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferVirusFlag.setStatus('optional')
xferSourceFile = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferSourceFile.setStatus('optional')
xferDestFile = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferDestFile.setStatus('optional')
hostEncryptionLevel = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostEncryptionLevel.setStatus('optional')
remoteEncryptionLevel = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteEncryptionLevel.setStatus('optional')
hostEndedReason = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostEndedReason.setStatus('optional')
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('optional')
xFerFailedFlag = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xFerFailedFlag.setStatus('optional')
encryptionErrorMessage = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionErrorMessage.setStatus('optional')
p3SerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p3SerialNumber.setStatus('optional')
systemName = MibScalar((1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemName.setStatus('optional')
pcaHostStarted = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,1)).setObjects(("PCA-Alert-MIB", "deviceType"), ("PCA-Alert-MIB", "hostConnectionObject"), ("PCA-Alert-MIB", "p3SerialNumber"), ("PCA-Alert-MIB", "systemName"))
pcaHostEndSession = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,2)).setObjects(("PCA-Alert-MIB", "hostEndedReason"), ("PCA-Alert-MIB", "systemName"))
pcaHostAbnormalEnd = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,3))
pcaHostConnFailDeviceError = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,4)).setObjects(("PCA-Alert-MIB", "deviceType"), ("PCA-Alert-MIB", "systemName"))
pcaHostStopped = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,5)).setObjects(("PCA-Alert-MIB", "hostEndedReason"), ("PCA-Alert-MIB", "systemName"))
pcaHostInSession = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,6)).setObjects(("PCA-Alert-MIB", "remoteComputerName"), ("PCA-Alert-MIB", "callerName"), ("PCA-Alert-MIB", "systemName"))
pcaHostConnFailAccessDenied = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,7)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaHostConnFailEncrypt = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,8)).setObjects(("PCA-Alert-MIB", "encryptionErrorMessage"), ("PCA-Alert-MIB", "systemName"))
pcaHostUnsecuredHostStarted = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,9)).setObjects(("PCA-Alert-MIB", "hostConnectionObject"), ("PCA-Alert-MIB", "systemName"))
pcaHostRebooting = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,10)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaHostLockingWorkstation = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,11)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaHostLoggingOffUser = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 1) + (0,12)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteStarted = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,1)).setObjects(("PCA-Alert-MIB", "deviceType"), ("PCA-Alert-MIB", "remoteConnectionObject"), ("PCA-Alert-MIB", "p3SerialNumber"), ("PCA-Alert-MIB", "systemName"))
pcaRemoteInSession = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,2)).setObjects(("PCA-Alert-MIB", "hostComputerName"), ("PCA-Alert-MIB", "systemName"))
pcaRemoteEndSession = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,3)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteAbnormalEndSession = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,4)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteConnFailDeviceError = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,5)).setObjects(("PCA-Alert-MIB", "deviceType"), ("PCA-Alert-MIB", "systemName"))
pcaRemoteConnFailHostBusy = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,6)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteConnFailHostNotFound = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,7)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteConnFailBadPassword = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,8)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaRemoteConnFailEncryption = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 2) + (0,9)).setObjects(("PCA-Alert-MIB", "encryptionErrorMessage"), ("PCA-Alert-MIB", "systemName"))
pcaFileXferStarted = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,1)).setObjects(("PCA-Alert-MIB", "hostComputerName"), ("PCA-Alert-MIB", "remoteComputerName"), ("PCA-Alert-MIB", "systemName"))
pcaFileXferEnded = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,2)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaFileXferAbnormalEnd = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,3)).setObjects(("PCA-Alert-MIB", "hostComputerName"), ("PCA-Alert-MIB", "remoteComputerName"), ("PCA-Alert-MIB", "systemName"))
pcaFileXferOperationCancelled = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,4)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaFileXferOperation = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,5)).setObjects(("PCA-Alert-MIB", "xferOperation"), ("PCA-Alert-MIB", "xferSourceFile"), ("PCA-Alert-MIB", "xferDestFile"), ("PCA-Alert-MIB", "xferBytes"), ("PCA-Alert-MIB", "xferVirusFlag"), ("PCA-Alert-MIB", "systemName"))
pcaFileXferVirusFound = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 3) + (0,6)).setObjects(("PCA-Alert-MIB", "xferSourceFile"), ("PCA-Alert-MIB", "systemName"))
pcaMonitorFullProductNotInstalled = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,1)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorHostNotInstalled = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,2)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorRemoteNotInstalled = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,3)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorHostNotWaiting = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,4)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorHostNotAutoStart = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,5)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorHostNotWaitingOnDialup = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,6)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorHostLanOnlyNotInstalled = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,7)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaMonitorLiveUpdateNotRun = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 5) + (0,8)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaResetNotInstalledReset = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 7) + (0,1)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaResetHostNotWaitingReset = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 7) + (0,2)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaResetHostNotAutoStartReset = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 7) + (0,3)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaResetHostWaitingOnDialupReset = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 7) + (0,4)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaResetLiveUpdateNotRunReset = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 7) + (0,5)).setObjects(("PCA-Alert-MIB", "systemName"))
pcaInstallRebootRequired = NotificationType((1, 3, 6, 1, 4, 1, 393, 100, 9, 6) + (0,1)).setObjects(("PCA-Alert-MIB", "systemName"))
mibBuilder.exportSymbols("PCA-Alert-MIB", hostConnectionObject=hostConnectionObject, pcaRemoteConnFailHostNotFound=pcaRemoteConnFailHostNotFound, pcaFileXferStarted=pcaFileXferStarted, pcaHostEndSession=pcaHostEndSession, hostComputerName=hostComputerName, pcaHostConnFailDeviceError=pcaHostConnFailDeviceError, pcaMonitorHostNotInstalled=pcaMonitorHostNotInstalled, pcaRemoteConnFailDeviceError=pcaRemoteConnFailDeviceError, xferSourceFile=xferSourceFile, pcaMonitorFullProductNotInstalled=pcaMonitorFullProductNotInstalled, pcaFileXferVirusFound=pcaFileXferVirusFound, pcaResetHostWaitingOnDialupReset=pcaResetHostWaitingOnDialupReset, pcaInstallRebootRequired=pcaInstallRebootRequired, pcaRemote=pcaRemote, pcaHost=pcaHost, p3SerialNumber=p3SerialNumber, pcaHostLoggingOffUser=pcaHostLoggingOffUser, pcaObject=pcaObject, xferFiles=xferFiles, remoteComputerName=remoteComputerName, systemName=systemName, xferDestFile=xferDestFile, remoteEncryptionLevel=remoteEncryptionLevel, xferBytes=xferBytes, hostEndedReason=hostEndedReason, pcaFileXferEnded=pcaFileXferEnded, pcaResetHostNotWaitingReset=pcaResetHostNotWaitingReset, pcaResetNotInstalledReset=pcaResetNotInstalledReset, pcaMonitorRemoteNotInstalled=pcaMonitorRemoteNotInstalled, pcaInstall=pcaInstall, pcaFileXfer=pcaFileXfer, pcaLDAP=pcaLDAP, xFerFailedFlag=xFerFailedFlag, pcaMonitorLiveUpdateNotRun=pcaMonitorLiveUpdateNotRun, pcaRemoteInSession=pcaRemoteInSession, pcaResetHostNotAutoStartReset=pcaResetHostNotAutoStartReset, pcaFileXferOperation=pcaFileXferOperation, pcaReset=pcaReset, pcaFileXferOperationCancelled=pcaFileXferOperationCancelled, remoteConnectionObject=remoteConnectionObject, pcaMonitorHostNotWaiting=pcaMonitorHostNotWaiting, pcaRemoteEndSession=pcaRemoteEndSession, pcaHostInSession=pcaHostInSession, pcaMonitorHostLanOnlyNotInstalled=pcaMonitorHostLanOnlyNotInstalled, pcaHostLockingWorkstation=pcaHostLockingWorkstation, pcaRemoteConnFailBadPassword=pcaRemoteConnFailBadPassword, hostEncryptionLevel=hostEncryptionLevel, encryptionErrorMessage=encryptionErrorMessage, pcaversionnine=pcaversionnine, pcaHostAbnormalEnd=pcaHostAbnormalEnd, xferOperation=xferOperation, pcaRemoteAbnormalEndSession=pcaRemoteAbnormalEndSession, pcaRemoteConnFailHostBusy=pcaRemoteConnFailHostBusy, pcaMonitorHostNotWaitingOnDialup=pcaMonitorHostNotWaitingOnDialup, pcaHostUnsecuredHostStarted=pcaHostUnsecuredHostStarted, pcaFileXferAbnormalEnd=pcaFileXferAbnormalEnd, pcaMonitorHostNotAutoStart=pcaMonitorHostNotAutoStart, pcaHostRebooting=pcaHostRebooting, pcaResetLiveUpdateNotRunReset=pcaResetLiveUpdateNotRunReset, pcanywhere=pcanywhere, pcaHostConnFailAccessDenied=pcaHostConnFailAccessDenied, pcaHostStopped=pcaHostStopped, pcaHostConnFailEncrypt=pcaHostConnFailEncrypt, deviceType=deviceType, pcaRemoteConnFailEncryption=pcaRemoteConnFailEncryption, symantec=symantec, callerName=callerName, pcaMonitor=pcaMonitor, pcaHostStarted=pcaHostStarted, pcaGateway=pcaGateway, xferVirusFlag=xferVirusFlag, pcaRemoteStarted=pcaRemoteStarted)