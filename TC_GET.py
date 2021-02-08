import sys
import os
import time
import csv

current_dir = os.path.split(os.path.realpath(__file__))[0]
if current_dir not in sys.path:
    sys.path.append(current_dir)

import StcPython as zte
import TC_SCAN as scan
######################################

stc = zte.StcPython()
testcenterver = stc.get("system1", "version")

######################################


def get_sn_to_csv(tclist, fname):
    # 初始化
    # szChassisIpList = zte.readtxt('ChassisIpList.py')
    # szChassisIpList = ('172.29.93.202', '172.29.97.54')
    print("  [-] Spirent TestCenter version : ", testcenterver)
    print('  [-] SN/PN in list: ', tclist)
    chassisLocationList = []
    chassisInfoDict = {}
    pchassisInfoDict = {}
    tmLocationList = []
    tmInfoDict = {}
    ptmInfoDict = {}
    timestamp = time.strftime('%Y.%m.%d.%H.%M.%S')

    for szChassisIp in tclist:
        try:
            print('  [-] Connect to TestCenter Chassis : ', szChassisIp)
            stc.connect(szChassisIp)
        except:
            continue
    # 获取 Chassis 信息
    hChassisList = getChassis()
    # print('hChassisList: ', hChassisList)
    for hChassis in hChassisList:
        chassisProps = stc.get(hChassis)
        chassisIpAddr = chassisProps['Hostname']
        chassisPartNum = chassisProps['PartNum']
        chassisSerialNum = chassisProps['SerialNum']
        chassisFirmwareVersion = chassisProps['FirmwareVersion']
        chassisLocation = '//%s' % chassisIpAddr
        chassisLocationList.append(chassisLocation)
        pszTemp = '{:<24}{:<24}{:<19}{:<15}{:<20}'.format(chassisLocation, chassisIpAddr, chassisPartNum, chassisSerialNum,
                                                          chassisFirmwareVersion)
        szTemp = (chassisLocation, chassisIpAddr, chassisPartNum, chassisSerialNum,
                  chassisFirmwareVersion)
        pchassisInfoDict[chassisLocation] = pszTemp
        chassisInfoDict[chassisLocation] = szTemp

        # 获取 TestModules 信息
        hTmList = getTestModules(hChassis)
        for hTm in hTmList:
            tmProps = stc.get(hTm)
            tmPartNum = tmProps['PartNum']
            tmSlotIndex = tmProps['Index']
            tmSerialNum = tmProps['SerialNum']
            tmFirmwareVersion = tmProps['FirmwareVersion']
            tmLocation = '//%s/%s' % (chassisIpAddr, tmSlotIndex)
            tmLocationList.append(tmLocation)
            pszTemp = '{:<24}{:<24}{:<19}{:<15}{:<20}'.format(
                tmLocation, chassisIpAddr, tmPartNum, tmSerialNum, tmFirmwareVersion)
            szTemp = (tmLocation, chassisIpAddr, tmPartNum,
                      tmSerialNum, tmFirmwareVersion)
            ptmInfoDict[tmLocation] = pszTemp
            tmInfoDict[tmLocation] = szTemp

    print('  [-] Collect TestCenter SerialNum Info ...')
    # 编写文件抬头
    item1 = r'Location'
    item2 = r'Chassis IP or Hostname'
    item3 = r'PartNum'
    item4 = r'Serial Number'
    item5 = r'FirmwareVersion'
    item = '{:<24}{:<24}{:<19}{:<15}{:<20}'.format(
        item1, item2, item3, item4, item5)
    parting_line = '============================================================================'

    # filename = 'TestCenter_SerialNum_info_' + timestamp + '.txt'
    filename = fname
    with open(filename, 'w', newline='') as csvfile:
        # f.write(item + '\r\n')
        # f.write(parting_line + '\r\n')
        # for chassisLocation in chassisLocationList:
        #     f.write(chassisInfoDict[chassisLocation] + '\r\n')
        # f.write(parting_line + '\r\n')
        # for tmLocation in tmLocationList:
        #     f.write(tmInfoDict[tmLocation] + '\r\n')
        fieldnames = [item1, item2, item3, item4, item5]
        print('  [-] Write Data to csvfile', filename)
        writer = csv.writer(csvfile)
        print(item)
        writer.writerow(['# Equipment Information'])
        writer.writerow(['# Generated on. '+timestamp])
        writer.writerow(['# Framework ver. '+testcenterver])
        writer.writerow([''])
        writer.writerow([''])
        writer.writerow(['# Chassis'])
        writer.writerow(fieldnames)
        print(parting_line)
        for chassisLocation in chassisLocationList:
            writer.writerow(chassisInfoDict[chassisLocation])
            print(pchassisInfoDict[chassisLocation])
        writer.writerow([''])
        writer.writerow(['# Test Module'])
        writer.writerow(fieldnames)
        print(parting_line)
        for tmLocation in tmLocationList:
            writer.writerow(tmInfoDict[tmLocation])
            print(ptmInfoDict[tmLocation])

    # with open(filename, 'r', newline='') as file:
    #     csvreader = csv.reader(file)
    #     # read csv file
    #     for row in csvreader:
    #         print('Aread line: ', row, len(row))

    print('  [-] Write to CSV finished')
    stc.perform("ChassisDisconnectAll")
    print('  [-] Collect TestCenter SerialNum Info Finished! ...')


def getChassisManager():
    return stc.get('system1', 'children-PhysicalChassisManager')


def getChassis():
    hMgr = getChassisManager()
    Chassis = stc.get(hMgr, 'children-PhysicalChassis')
    return Chassis.split()


def getTestModules(hChassis):
    TestModules = stc.get(hChassis, 'children-PhysicalTestmodule')
    return TestModules.split()


def getPortGroups(hTm):
    PortGroups = stc.get(hTm, 'children-PhysicalPortgroup')
    return PortGroups.split()


def getPorts(hPg):
    Ports = stc.get(hPg, 'children-PhysicalPort')
    return Ports.split()


def getEthernetFiber(hPort):
    return stc.get(hPort, 'EthernetFiber')


def displayChassisInfo(hChassis):
    chassisProps = stc.get(hChassis)
    print(chassisProps['SerialNum'])


def displayEthernetFiberInfo(hEthernetFiber):
    fiberProps = stc.get(hEthernetFiber)
    print(fiberProps['ModuleType'])
    print(fiberProps['VendorName'])
    print(fiberProps['VendorSerialNumber'])


# get_sn('test.csv')
