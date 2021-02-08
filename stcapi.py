# Spirent TestCenter Logic Script
# Generated on Mon Nov  9 17:32:55 2020 by labpc
# Framework ver. 5.15.0086.0000
#
# Comments: 
# 
#
# This logic script contains the following routines invoked from the
# 123.py script.



# Load Spirent TestCenter
from StcPython import StcPython
stc = StcPython()

#    init - set the logging level and logging location (stdout).
#           Possible logLevel values are: 
#             DEBUG - Display DEBUG, INFO, WARN, and ERROR messages
#             INFO  - Display INFO, WARN, and ERROR messages
#             WARN  - Display WARN and ERROR messages
#             ERROR - Display only ERROR messages
#
#           Possible values for logTo are "stdout" or a file name (can include
#           the path). Use forward slashes between directory names.
def init():
    stc.config('automationoptions', logTo='stdout', logLevel='WARN')

#    config - load the configuration into memory. The port locations
#             are taken from the XML file but may be passed in from the
#             launcher script. The XML config file may be passed in from
#             the launcher script as well.
#
#           - set the location for results files.
#             Possible values are: 
#               INSTALL_DIR - Spirent TestCenter installation directory.
#               CURRENT_WORKING_DIR - Current working directory. This 
#                   is the directory that Spirent TestCenter currently
#                   has open.
#               USER_WORKING_DIR - User working directory.
#               CURRENT_CONFIG_DIR - Current configuration directory. 
#                   This is the directory where the saved or loaded
#                   .xml or .tcc file is located. If no .xml or .tcc 
#                   file has been saved or loaded, files are saved
#                   to the user working directory.
#
#             The location of the results files can be modified in the
#             launcher file. The saveResultsRelativeTo parameter sets a path 
#             that is prepended to the value of the ResultsDirectory 
#             parameter. To set an fully qualified (absolute) path for 
#             results, set the ResultsDirectory parameter and set 
#             SaveResultsRelativeTo to NONE.
#
#           - set up the sequencer. Currently sets the sequencer
#             to stop on any error.  Other options are IGNORE_ERROR and 
#             PAUSE_ON_ERROR.
def config(resultsDir, portLocations):
    stc.config('system1',IsLoadingFromConfiguration='true')

    system1 = "system1"
    stc.config('system1', \
    InSimulationMode="FALSE", \
    UseSmbMessaging="FALSE", \
    ApplicationName="TestCenter", \
    TSharkPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StcSystem 1")

    Project_1 = stc.create("Project", \
    TableViewData="", \
    TestMode="L2L3", \
    SelectedTechnologyProfiles="", \
    ConfigurationFileName="123.py", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Project 1")

    FrameLengthDistribution_1 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Default")

    FrameLengthDistributionSlot_1 = (stc.get( FrameLengthDistribution_1, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 5")

    FrameLengthDistributionSlot_2 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 6")

    FrameLengthDistributionSlot_3 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 7")

    FrameLengthDistribution_2 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Spirent")

    FrameLengthDistributionSlot_4 = (stc.get( FrameLengthDistribution_2, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 13")

    FrameLengthDistributionSlot_5 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="44", \
    MinFrameLength="43", \
    MaxFrameLength="45", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 14")

    FrameLengthDistributionSlot_6 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 15")

    FrameLengthDistributionSlot_7 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 16")

    FrameLengthDistribution_3 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="4-Point")

    FrameLengthDistributionSlot_8 = (stc.get( FrameLengthDistribution_3, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_8, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="55", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 8")

    FrameLengthDistributionSlot_9 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="15", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 9")

    FrameLengthDistributionSlot_10 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 10")

    FrameLengthDistributionSlot_11 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="RANDOM", \
    FixedFrameLength="730", \
    MinFrameLength="40", \
    MaxFrameLength="1500", \
    Weight="20", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 11")

    FrameLengthDistribution_4 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TCPv4")

    FrameLengthDistributionSlot_12 = (stc.get( FrameLengthDistribution_4, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_12, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 17")

    FrameLengthDistributionSlot_13 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 18")

    FrameLengthDistributionSlot_14 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 19")

    FrameLengthDistributionSlot_15 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 20")

    FrameLengthDistribution_5 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPSEC")

    FrameLengthDistributionSlot_16 = (stc.get( FrameLengthDistribution_5, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_16, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 21")

    FrameLengthDistributionSlot_17 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 22")

    FrameLengthDistributionSlot_18 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 23")

    FrameLengthDistributionSlot_19 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1400", \
    MinFrameLength="1399", \
    MaxFrameLength="1401", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 24")

    FrameLengthDistribution_6 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Downstream")

    FrameLengthDistributionSlot_20 = (stc.get( FrameLengthDistribution_6, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_20, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 53")

    FrameLengthDistributionSlot_21 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 54")

    FrameLengthDistributionSlot_22 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 55")

    FrameLengthDistributionSlot_23 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="5", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 56")

    FrameLengthDistribution_7 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Upstream")

    FrameLengthDistributionSlot_24 = (stc.get( FrameLengthDistribution_7, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_24, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 49")

    FrameLengthDistributionSlot_25 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="8", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 50")

    FrameLengthDistributionSlot_26 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 51")

    FrameLengthDistributionSlot_27 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 52")

    CustomFillPattern_1 = stc.create("CustomFillPattern",under = Project_1, \
    PatternData="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Pattern 1")

    Tags_1 = (stc.get( Project_1, 'children-Tags' )).split(' ')[0]
    stc.config(Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Tags 1")

    Tag_1 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    Tag_2 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Router")

    Tag_3 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Client")

    Tag_4 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Server")

    Tag_5 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Core")

    Tag_6 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Edge")

    DeviceAddrOptions_1 = (stc.get( Project_1, 'children-DeviceAddrOptions' )).split(' ')[0]
    stc.config(DeviceAddrOptions_1, \
    NextIpv4="192.85.1.3", \
    Ipv4Increment="0.0.0.1", \
    DefaultIpv4Prefix="24", \
    NextIpv6="2001::2", \
    Ipv6Increment="::1", \
    DefaultIpv6Prefix="64", \
    NextMac="00:10:94:00:00:01", \
    MacIncrement="00:00:00:00:00:01", \
    NextRouterId="192.0.0.1", \
    RouterIdIncrement="0.0.0.1", \
    NextIpv6RouterId="2000::1", \
    Ipv6RouterIdIncrement="::1", \
    NextWwn="20:00:10:85:00:00:00:01", \
    WwnIncrement="00:00:00:00:00:00:00:01", \
    UseForDeviceGenConfigExpand="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceAddrOptions 1")

    Ieee80211PhyOptions_1 = (stc.get( Project_1, 'children-Ieee80211PhyOptions' )).split(' ')[0]
    stc.config(Ieee80211PhyOptions_1, \
    SelectedRegion="USA", \
    AutoConnect="FALSE", \
    ScanDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee80211PhyOptions 1")

    PhyOptions_1 = (stc.get( Project_1, 'children-PhyOptions' )).split(' ')[0]
    stc.config(PhyOptions_1, \
    EnableCompensationMode="FALSE", \
    Enable8023brSwitch="FALSE", \
    EnableL1RegisterAccess="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhyOptions 1")

    TestResultSetting_1 = (stc.get( Project_1, 'children-TestResultSetting' )).split(' ')[0]
    stc.config(TestResultSetting_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestResultSetting 1")

    TestInfo_1 = (stc.get( Project_1, 'children-TestInfo' )).split(' ')[0]
    stc.config(TestInfo_1, \
    OwnerDisplayName="", \
    TestName="", \
    Description="", \
    UserTags="", \
    WebUILaunched="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestInfo 1")

    PortOptions_1 = (stc.get( Project_1, 'children-PortOptions' )).split(' ')[0]
    stc.config(PortOptions_1, \
    ReleaseMode="FULL_RESET", \
    AggregatorResult="AGGREGATED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Port Options 1")

    RealismOptions_1 = (stc.get( Project_1, 'children-RealismOptions' )).split(' ')[0]
    stc.config(RealismOptions_1, \
    RealismMode="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Realism Options 1")

    EventPublisherConfig_1 = (stc.get( Project_1, 'children-EventPublisherConfig' )).split(' ')[0]
    stc.config(EventPublisherConfig_1, \
    IsEnabled="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EventPublisherConfig 1")

    TrafficOptions_1 = (stc.get( Project_1, 'children-TrafficOptions' )).split(' ')[0]
    stc.config(TrafficOptions_1, \
    TrafficStartMode="ASYNCHRONOUS", \
    TrafficStartInterval="0", \
    TrafficStartIntervalUnit="UNITOF64US", \
    TrafficStreamIDStartIndex="1", \
    DeleteInactiveStreamsFromMemory="FALSE", \
    EnableGlobalAnalyzerPreload="FALSE", \
    TSharkPath="None", \
    ExcludeEthernetFcs="TRUE", \
    SmoothenRandomLength="FALSE", \
    UniqueRandomLengthSeedPerPort="FALSE", \
    EnableTxQueueFullRetryMode="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TrafficOptions 1")

    GroupHistogram_1 = (stc.get( Project_1, 'children-GroupHistogram' )).split(' ')[0]
    stc.config(GroupHistogram_1, \
    ActiveGroupHistogramMode="DISABLED_MODE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Group Histogram 1")

    ResultOptions_1 = (stc.get( Project_1, 'children-ResultOptions' )).split(' ')[0]
    stc.config(ResultOptions_1, \
    ResultViewMode="BASIC", \
    ColumnFilterMode="BASIC", \
    ShowWarningMessage="TRUE", \
    StopTrafficBeforeClearingResults="FALSE", \
    StopAnalyzerBeforeClearingResults="FALSE", \
    SyncClearResults="FALSE", \
    TimedRefreshResultViewMode="MANUAL", \
    TimedRefreshInterval="10", \
    CollectStrayFrame="FALSE", \
    PreambleByteLength="8", \
    IfgByteLength="12", \
    JitterMode="RFC3393ABSOLUTEVALUE", \
    DeleteAllAnalyzerStreams="FALSE", \
    SaveAtEotProperties="", \
    TxPortExpectMCastTrafficSentFromSelf="FALSE", \
    SaveOnlyCountersFromResultViewMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultOptions 1")

    LabelBindingGlobalConfig_1 = (stc.get( Project_1, 'children-LabelBindingGlobalConfig' )).split(' ')[0]
    stc.config(LabelBindingGlobalConfig_1, \
    SubscriptionInterval="5", \
    LabelResolutionMode="PER_SESSION_LABEL_RESOLUTION", \
    SelectDeactivedTunnelForData="TRUE", \
    EnableTransmitUnresolvedStream="TRUE", \
    EnableStaticPwAttachmentGroupId="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LabelBindingGlobalConfig 1")

    MplsTpGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpGlobalConfig_1, \
    FMChannelType="88", \
    PWChannelType="34", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpGlobalConfig 1")

    L2LearningConfig_1 = (stc.get( Project_1, 'children-L2LearningConfig' )).split(' ')[0]
    stc.config(L2LearningConfig_1, \
    Rate="1000", \
    RepeatCount="3", \
    LearningStartDelay="1", \
    L2FrameSize="SAME_AS_STREAM", \
    L2FrameSizeFixed="128", \
    EncapOption="USE_TX_ENCAP", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2LearningConfig 1")

    ArpNdConfig_1 = (stc.get( Project_1, 'children-ArpNdConfig' )).split(' ')[0]
    stc.config(ArpNdConfig_1, \
    LearningRate="250", \
    MaxBurst="16", \
    EnableCyclicArp="TRUE", \
    DuplicateGatewayDetection="TRUE", \
    RetryCount="3", \
    TimeOut="1000", \
    EnableUniqueMacAddrInReply="FALSE", \
    EnableUniqueMacPattern="2222", \
    ProcessGratuitousArpRequests="TRUE", \
    UpdateDestMacUponNonGratuitousArpRequestsReceived="FALSE", \
    ProcessUnsolicitedArpReplies="TRUE", \
    EnableAutoArp="FALSE", \
    ApplyConfiguredGatewayMac="FALSE", \
    SetArpNdNoExpire="FALSE", \
    IgnoreFailures="TRUE", \
    UseLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseConfiguredLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseLinklayerCacheInStack="FALSE", \
    NeighborAdvertismentAlwaysOverrides="FALSE", \
    UseGatewayForTarget="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdConfig 1")

    BgpGlobalConfig_1 = (stc.get( Project_1, 'children-BgpGlobalConfig' )).split(' ')[0]
    stc.config(BgpGlobalConfig_1, \
    SequentialStartup="DISABLE", \
    StaggerOpen="100", \
    StaggerClose="100", \
    ConnectionRetryInterval="30", \
    ConnectionRetryCount="100", \
    UpdateCount="2000", \
    UpdateDelay="1", \
    VplsDraftVersion="VERSION_VPLS_4761", \
    ScalabilityMode="NORMAL", \
    EnableTcpNoDelay="FALSE", \
    EnablePackUpdates="TRUE", \
    TxTcpBufferSize="TCPBUFFER_32KB", \
    RxTcpBufferSize="TCPBUFFER_32KB", \
    TcpMaxSegmentSize="1460", \
    EnableStraightforwardUpdate="FALSE", \
    IgnoreAttributeErrors="FALSE", \
    MvpnAutoAdvertiseDelay="1000", \
    IsEvpnIRB="FALSE", \
    EnableEvpnLearningScaleMode="FALSE", \
    EvpnIRBMode="ASYMMETRIC", \
    NextHopFilterMode="DISABLED", \
    EnableDiscardUpdates="FALSE", \
    DisablePathMtuDiscovery="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpGlobalConfig 1")

    BgpSrGlobalConfig_1 = (stc.get( BgpGlobalConfig_1, 'children-BgpSrGlobalConfig' )).split(' ')[0]
    stc.config(BgpSrGlobalConfig_1, \
    SrDraftVersion="VERSION_00", \
    Srv6DraftVersion="VERSION_05", \
    PrefixSidAttrType="40", \
    Srv6TlvType="5", \
    Srv6L2ServiceTlvType="6", \
    SrVpnTrafficBindingKey="RD", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalConfig 1")

    BgpSrGlobalBlock_1 = (stc.get( BgpSrGlobalConfig_1, 'children-BgpSrGlobalBlock' )).split(' ')[0]
    stc.config(BgpSrGlobalBlock_1, \
    BlockBase="16000", \
    BlockRange="1000", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalBlock 1")

    PimGlobalConfig_1 = (stc.get( Project_1, 'children-PimGlobalConfig' )).split(' ')[0]
    stc.config(PimGlobalConfig_1, \
    TriggerHelloDelay="5", \
    EnablingPruningDelayOption="FALSE", \
    Tbit="FALSE", \
    LanPruneDelay="500", \
    OverrideInterval="2500", \
    EnablePackGroupRecord="TRUE", \
    EnableMsgRate="FALSE", \
    MsgRate="100", \
    MsgInterval="1", \
    DisableHelloExpireTimer="FALSE", \
    DisableHelloRxInNeighborState="FALSE", \
    DisableIncomingMsgProcessing="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PimGlobalConfig 1")

    IsisGlobalConfig_1 = (stc.get( Project_1, 'children-IsisGlobalConfig' )).split(' ')[0]
    stc.config(IsisGlobalConfig_1, \
    ScalabilityMode="NORMAL", \
    UseSameSrgb="FALSE", \
    SrmsPreferenceSubTlvType="24", \
    Srv6CapabilitySubTlvType="25", \
    Srv6LocatorTlvType="27", \
    Srv6EndSidSubTlvType="5", \
    Srv6EndXSidSubTlvType="43", \
    Srv6LanEndXSidSubTlvType="44", \
    SrNodeMsdSubTlvType="23", \
    SrLinkMsdSubTlvType="15", \
    FapmSubTlvType="5", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisGlobalConfig 1")

    IsisPlsbGlobalConfig_1 = (stc.get( Project_1, 'children-IsisPlsbGlobalConfig' )).split(' ')[0]
    stc.config(IsisPlsbGlobalConfig_1, \
    PlsbNlpid="143", \
    PlsbInstanceTlvType="180", \
    PlsbIsidAddrTlvType="181", \
    PlsbLinkMetricSubTlvType="17", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisPlsbGlobalConfig 1")

    OtvOptions_1 = (stc.get( Project_1, 'children-OtvOptions' )).split(' ')[0]
    stc.config(OtvOptions_1, \
    UnicastOnlyTransport="FALSE", \
    OverlayEncapMode="MPLS_GRE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OTV Project-Level Options 1")

    VxlanGlobalConfig_1 = (stc.get( Project_1, 'children-VxlanGlobalConfig' )).split(' ')[0]
    stc.config(VxlanGlobalConfig_1, \
    EnableVxlanScale="TRUE", \
    EnableTrafficScaleForEvpnLearning="FALSE", \
    EnableVxlanFlowBasedTraffic="FALSE", \
    EnableEvpnOverlayIRB="FALSE", \
    EvpnOverlayIRBMode="ASYMMETRIC", \
    DiscardEvpnLearning="FALSE", \
    EnableDRVForVxlanBindings="FALSE", \
    EnableEvpnType5VA="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VxlanGlobalConfig 1")

    PcepGlobalConfig_1 = (stc.get( Project_1, 'children-PcepGlobalConfig' )).split(' ')[0]
    stc.config(PcepGlobalConfig_1, \
    SessionOutStanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    LSPPerMessage="100", \
    TCPInterval="500", \
    PacketAlignToMTU="FALSE", \
    EnableTCPNoDelay="FALSE", \
    UseSRDraft5="FALSE", \
    AssociationTypeListTlvType="200", \
    PpagAssociationType="100", \
    PpagTlvType="100", \
    PathSegmentTlvType="80", \
    PathBindingTlvType="81", \
    SRv6PCECapabilitySubTlvType="27", \
    SRv6EroSubObjectType="37", \
    SRv6RroSubObjectType="37", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PcepGlobalConfig 1")

    Ieee8021asGlobalConfig_1 = (stc.get( Project_1, 'children-Ieee8021asGlobalConfig' )).split(' ')[0]
    stc.config(Ieee8021asGlobalConfig_1, \
    ManagementId="12292", \
    TlvType="32772", \
    SlaveInfoSetCount="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee8021asGlobalConfig 1")

    Dhcpv4Options_1 = (stc.get( Project_1, 'children-Dhcpv4Options' )).split(' ')[0]
    stc.config(Dhcpv4Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4Options 1")

    Dhcpv6Options_1 = (stc.get( Project_1, 'children-Dhcpv6Options' )).split(' ')[0]
    stc.config(Dhcpv6Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6Options 1")

    PppoxOptions_1 = (stc.get( Project_1, 'children-PppoxOptions' )).split(' ')[0]
    stc.config(PppoxOptions_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_CONNECTED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxOptions 1")

    CuspGlobalConfig_1 = (stc.get( Project_1, 'children-CuspGlobalConfig' )).split(' ')[0]
    stc.config(CuspGlobalConfig_1, \
    SessionRetryCount="10", \
    SessionRetryInterval="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CuspGlobalConfig 1")

    MplsTpOamGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpOamGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpOamGlobalConfig_1, \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    TstOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"MPLSTPOAMTLV:TestTLV\"><Length>0040</Length></pdu></pdus></config></frame>", \
    ChannelType="8902", \
    EchoTlvsInLmr="FALSE", \
    EchoTlvsInDmr="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpOamGlobalConfig 1")

    EoamGlobalConfig_1 = (stc.get( Project_1, 'children-EoamGlobalConfig' )).split(' ')[0]
    stc.config(EoamGlobalConfig_1, \
    DmCommonTimeSource="FALSE", \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    SlrTxFCbStart="1", \
    SlrTxFCbStep="1", \
    SlmTxFCfOffset="0", \
    SlrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LtmOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTMEgrID\"><Length>0000</Length></pdu></pdus></config></frame>", \
    LtrOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTREgrID\"><Length>0000</Length></pdu><pdu name=\"RplyEgr_1\" pdu=\"EOAMTLV:RplyEgr\"><Length>0000</Length></pdu></pdus></config></frame>", \
    DmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    DmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    ResultTimeUnit="MILLISECONDS", \
    TestModeType="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamGlobalConfig 1")

    VqAnalyzerOptions_1 = (stc.get( Project_1, 'children-VqAnalyzerOptions' )).split(' ')[0]
    stc.config(VqAnalyzerOptions_1, \
    SamplingPeriod="10", \
    DatabaseFileName="vqAnalyzerTest.db", \
    AppendDateTime="TRUE", \
    EnableEotDatabase="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzerOptions 1")

    ExternalDeviceOption_1 = (stc.get( Project_1, 'children-ExternalDeviceOption' )).split(' ')[0]
    stc.config(ExternalDeviceOption_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ExternalDeviceOption 1")

    Dot1xOptions_1 = (stc.get( Project_1, 'children-Dot1xOptions' )).split(' ')[0]
    stc.config(Dot1xOptions_1, \
    TrafficStartOption="IGNORE_AUTH", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dot1xOptions 1")

    VicGlobalConfig_1 = (stc.get( Project_1, 'children-VicGlobalConfig' )).split(' ')[0]
    stc.config(VicGlobalConfig_1, \
    OpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    CreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"><Type>12</Type><Length>0</Length><ProvisioningInfoTypeSpace>00000C</ProvisioningInfoTypeSpace><Info><ProvList name=\"ProvList_0\"><Fixed><NumOfTlvs>0</NumOfTlvs><SubTlvs><FixedSubTlvList name=\"FixedSubTlvList_0\"><ProfileNameTlv><Type>1</Type><Length>0</Length></ProfileNameTlv></FixedSubTlvList><FixedSubTlvList name=\"FixedSubTlvList_1\"><vNicUuidTlv><Type>2</Type><Length>0</Length></vNicUuidTlv></FixedSubTlvList></SubTlvs></Fixed></ProvList></Info></pdu></pdus></config></frame>", \
    EnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    SpirentOpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    SpirentCreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"></pdu></pdus></config></frame>", \
    SpirentEnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VIC 1")

    spirent_results_DutCollectorConfig_1 = (stc.get( Project_1, 'children-spirent.results.DutCollectorConfig' )).split(' ')[0]
    stc.config(spirent_results_DutCollectorConfig_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.DutCollectorConfig 1")

    spirent_results_SnmpTrap_1 = (stc.get( spirent_results_DutCollectorConfig_1, 'children-spirent.results.SnmpTrap' )).split(' ')[0]
    stc.config(spirent_results_SnmpTrap_1, \
    Enable="FALSE", \
    Transport="UDP", \
    Version="V2C", \
    CustomTraps="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.SnmpTrap 1")

    MsdpGlobalConfig_1 = (stc.get( Project_1, 'children-MsdpGlobalConfig' )).split(' ')[0]
    stc.config(MsdpGlobalConfig_1, \
    SessionOutstanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    SourceActiveAdvertisementTimer="60", \
    SourceActiveStateTimer="100", \
    PacketAlignToMTU="FALSE", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MsdpGlobalConfig 1")

    OamFlexeGlobalConfig_1 = (stc.get( Project_1, 'children-OamFlexeGlobalConfig' )).split(' ')[0]
    stc.config(OamFlexeGlobalConfig_1, \
    CodeO="75", \
    CodeC="12", \
    BasType="1", \
    ApsType="2", \
    CvType="17", \
    DmType="18", \
    DmmType="19", \
    DmmrType="20", \
    CsType="21", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OamFlexeGlobalConfig 1")

    ResultDataSet_1 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="Port", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="100", \
    NotifyInterval="1000", \
    Identifier="Port Traffic\\Basic Traffic Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/Port", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Basic Traffic Results")

    ResultQuery_1 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="generator", \
    ResultClassId="generatorportresults", \
    PropertyIdArray="generatorportresults.totalframecount generatorportresults.totaloctetcount generatorportresults.generatorframecount generatorportresults.generatoroctetcount generatorportresults.generatorsigframecount generatorportresults.generatorundersizeframecount generatorportresults.generatoroversizeframecount generatorportresults.generatorjumboframecount generatorportresults.totalframerate generatorportresults.totaloctetrate generatorportresults.generatorframerate generatorportresults.generatoroctetrate generatorportresults.generatorsigframerate generatorportresults.generatorundersizeframerate generatorportresults.generatoroversizeframerate generatorportresults.generatorjumboframerate generatorportresults.generatorcrcerrorframecount generatorportresults.generatorl3checksumerrorcount generatorportresults.generatorl4checksumerrorcount generatorportresults.generatorcrcerrorframerate generatorportresults.generatorl3checksumerrorrate generatorportresults.generatorl4checksumerrorrate generatorportresults.totalipv4framecount generatorportresults.totalipv6framecount generatorportresults.totalmplsframecount generatorportresults.generatoripv4framecount generatorportresults.generatoripv6framecount generatorportresults.generatorvlanframecount generatorportresults.generatormplsframecount generatorportresults.totalipv4framerate generatorportresults.totalipv6framerate generatorportresults.totalmplsframerate generatorportresults.generatoripv4framerate generatorportresults.generatoripv6framerate generatorportresults.generatorvlanframerate generatorportresults.generatormplsframerate generatorportresults.totalbitrate generatorportresults.generatorbitrate generatorportresults.l1bitcount generatorportresults.l1bitrate generatorportresults.pfcframecount generatorportresults.pfcpri0framecount generatorportresults.pfcpri1framecount generatorportresults.pfcpri2framecount generatorportresults.pfcpri3framecount generatorportresults.pfcpri4framecount generatorportresults.pfcpri5framecount generatorportresults.pfcpri6framecount generatorportresults.pfcpri7framecount generatorportresults.txqueuefulldropcount generatorportresults.txqueuefullretrycount generatorportresults.l1bitratepercent", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 32")

    ResultQuery_2 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="analyzer", \
    ResultClassId="analyzerportresults", \
    PropertyIdArray="analyzerportresults.totalframecount analyzerportresults.totaloctetcount analyzerportresults.sigframecount analyzerportresults.undersizeframecount analyzerportresults.oversizeframecount analyzerportresults.jumboframecount analyzerportresults.minframelength analyzerportresults.maxframelength analyzerportresults.pauseframecount analyzerportresults.totalframerate analyzerportresults.totaloctetrate analyzerportresults.sigframerate analyzerportresults.undersizeframerate analyzerportresults.oversizeframerate analyzerportresults.jumboframerate analyzerportresults.pauseframerate analyzerportresults.fcserrorframecount analyzerportresults.ipv4checksumerrorcount analyzerportresults.tcpchecksumerrorcount analyzerportresults.udpchecksumerrorcount analyzerportresults.prbsfilloctetcount analyzerportresults.prbsbiterrorcount analyzerportresults.fcserrorframerate analyzerportresults.ipv4checksumerrorrate analyzerportresults.tcpchecksumerrorrate analyzerportresults.udpchecksumerrorrate analyzerportresults.prbsfilloctetrate analyzerportresults.prbsbiterrorrate analyzerportresults.ipv4framecount analyzerportresults.ipv6framecount analyzerportresults.ipv6overipv4framecount analyzerportresults.tcpframecount analyzerportresults.udpframecount analyzerportresults.mplsframecount analyzerportresults.icmpframecount analyzerportresults.vlanframecount analyzerportresults.ipv4framerate analyzerportresults.ipv6framerate analyzerportresults.ipv6overipv4framerate analyzerportresults.tcpframerate analyzerportresults.udpframerate analyzerportresults.mplsframerate analyzerportresults.icmpframerate analyzerportresults.vlanframerate analyzerportresults.trigger1count analyzerportresults.trigger1rate analyzerportresults.trigger2count analyzerportresults.trigger2rate analyzerportresults.trigger3count analyzerportresults.trigger3rate analyzerportresults.trigger4count analyzerportresults.trigger4rate analyzerportresults.trigger5count analyzerportresults.trigger5rate analyzerportresults.trigger6count analyzerportresults.trigger6rate analyzerportresults.trigger7count analyzerportresults.trigger7rate analyzerportresults.trigger8count analyzerportresults.trigger8rate analyzerportresults.combotriggercount analyzerportresults.combotriggerrate analyzerportresults.totalbitrate analyzerportresults.prbsbiterrorratio analyzerportresults.vlanframerate analyzerportresults.l1bitcount analyzerportresults.l1bitrate analyzerportresults.pfcframecount analyzerportresults.fcoeframecount analyzerportresults.pfcframerate analyzerportresults.fcoeframerate analyzerportresults.pfcpri0framecount analyzerportresults.pfcpri1framecount analyzerportresults.pfcpri2framecount analyzerportresults.pfcpri3framecount analyzerportresults.pfcpri4framecount analyzerportresults.pfcpri5framecount analyzerportresults.pfcpri6framecount analyzerportresults.pfcpri7framecount analyzerportresults.pfcpri0quanta analyzerportresults.pfcpri1quanta analyzerportresults.pfcpri2quanta analyzerportresults.pfcpri3quanta analyzerportresults.pfcpri4quanta analyzerportresults.pfcpri5quanta analyzerportresults.pfcpri6quanta analyzerportresults.pfcpri7quanta analyzerportresults.prbserrorframecount analyzerportresults.prbserrorframerate analyzerportresults.userdefinedframecount1 analyzerportresults.userdefinedframerate1 analyzerportresults.userdefinedframecount2 analyzerportresults.userdefinedframerate2 analyzerportresults.userdefinedframecount3 analyzerportresults.userdefinedframerate3 analyzerportresults.userdefinedframecount4 analyzerportresults.userdefinedframerate4 analyzerportresults.userdefinedframecount5 analyzerportresults.userdefinedframerate5 analyzerportresults.userdefinedframecount6 analyzerportresults.userdefinedframerate6 analyzerportresults.avglatency analyzerportresults.minlatency analyzerportresults.maxlatency analyzerportresults.totallatency analyzerportresults.l1bitratepercent analyzerportresults.outseqframecount analyzerportresults.preambletotalbytes analyzerportresults.preambleminlength analyzerportresults.preamblemaxlength analyzerportresults.droppedframecount analyzerportresults.inorderframecount analyzerportresults.reorderedframecount analyzerportresults.duplicateframecount analyzerportresults.lateframecount analyzerportresults.firstarrivaltime analyzerportresults.lastarrivaltime analyzerportresults.correctedrsfecerrorcount analyzerportresults.uncorrectedrsfecerrorcount analyzerportresults.correctedbaserfecerrorcount analyzerportresults.uncorrectedbaserfecerrorcount analyzerportresults.correctedrsfecsymbols analyzerportresults.prersfecserrate analyzerportresults.postrsfecserrate analyzerportresults.prebaserfecserrate analyzerportresults.postbaserfecserrate", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 33")

    RealTimeResultColumnDefinition_1 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 671")

    RealTimeResultColumnDefinition_2 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 672")

    RealTimeResultColumnDefinition_3 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 673")

    RealTimeResultColumnDefinition_4 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 674")

    RealTimeResultColumnDefinition_5 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 675")

    RealTimeResultColumnDefinition_6 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 676")

    RealTimeResultColumnDefinition_7 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 677")

    RealTimeResultColumnDefinition_8 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 678")

    RealTimeResultColumnDefinition_9 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 679")

    RealTimeResultColumnDefinition_10 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_11 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_12 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_13 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_14 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 682")

    RealTimeResultColumnDefinition_15 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="167", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 683")

    RealTimeResultColumnDefinition_16 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="130", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 684")

    RealTimeResultColumnDefinition_17 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 685")

    RealTimeResultColumnDefinition_18 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 686")

    RealTimeResultColumnDefinition_19 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 687")

    RealTimeResultColumnDefinition_20 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOctetRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 688")

    RealTimeResultColumnDefinition_21 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="131", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 689")

    RealTimeResultColumnDefinition_22 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="139", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 690")

    RealTimeResultColumnDefinition_23 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="102", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 691")

    RealTimeResultColumnDefinition_24 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="197", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 692")

    RealTimeResultColumnDefinition_25 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="201", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 693")

    RealTimeResultColumnDefinition_26 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 694")

    RealTimeResultColumnDefinition_27 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 695")

    RealTimeResultColumnDefinition_28 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="171", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 696")

    RealTimeResultColumnDefinition_29 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="168", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 697")

    RealTimeResultColumnDefinition_30 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="170", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 698")

    RealTimeResultColumnDefinition_31 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsFillOctetCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 699")

    RealTimeResultColumnDefinition_32 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="137", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 700")

    RealTimeResultColumnDefinition_33 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRatio", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 701")

    RealTimeResultColumnDefinition_34 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="134", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 702")

    RealTimeResultColumnDefinition_35 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="172", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 703")

    RealTimeResultColumnDefinition_36 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 704")

    RealTimeResultColumnDefinition_37 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 705")

    RealTimeResultColumnDefinition_38 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="164", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 706")

    RealTimeResultColumnDefinition_39 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="162", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 707")

    RealTimeResultColumnDefinition_40 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="163", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 708")

    RealTimeResultColumnDefinition_41 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="169", \
    ColumnUnits="5", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 709")

    RealTimeResultColumnDefinition_42 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 710")

    RealTimeResultColumnDefinition_43 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 711")

    RealTimeResultColumnDefinition_44 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 712")

    RealTimeResultColumnDefinition_45 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 713")

    RealTimeResultColumnDefinition_46 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 714")

    RealTimeResultColumnDefinition_47 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 715")

    RealTimeResultColumnDefinition_48 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 716")

    RealTimeResultColumnDefinition_49 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 717")

    RealTimeResultColumnDefinition_50 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="87", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 718")

    RealTimeResultColumnDefinition_51 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 719")

    RealTimeResultColumnDefinition_52 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 720")

    RealTimeResultColumnDefinition_53 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 721")

    RealTimeResultColumnDefinition_54 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 722")

    RealTimeResultColumnDefinition_55 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 723")

    RealTimeResultColumnDefinition_56 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 724")

    RealTimeResultColumnDefinition_57 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 725")

    RealTimeResultColumnDefinition_58 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 726")

    RealTimeResultColumnDefinition_59 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="114", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 727")

    RealTimeResultColumnDefinition_60 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="86", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 728")

    RealTimeResultColumnDefinition_61 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="88", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 729")

    RealTimeResultColumnDefinition_62 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="91", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 730")

    RealTimeResultColumnDefinition_63 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="129", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 731")

    RealTimeResultColumnDefinition_64 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 732")

    RealTimeResultColumnDefinition_65 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 733")

    RealTimeResultColumnDefinition_66 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="132", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 734")

    RealTimeResultColumnDefinition_67 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 735")

    RealTimeResultColumnDefinition_68 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="124", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 736")

    RealTimeResultColumnDefinition_69 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 737")

    RealTimeResultColumnDefinition_70 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 738")

    RealTimeResultColumnDefinition_71 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 739")

    RealTimeResultColumnDefinition_72 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 740")

    RealTimeResultColumnDefinition_73 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="113", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 741")

    RealTimeResultColumnDefinition_74 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="87", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 742")

    RealTimeResultColumnDefinition_75 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="96", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 743")

    RealTimeResultColumnDefinition_76 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="99", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 744")

    RealTimeResultGroupDefinition_1 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="All Groups", \
    GroupId="core://allgroups/", \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    CountQuery="", \
    SqlString="", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 37")

    RealTimeResultColumnDefinition_77 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="101", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 38")

    RealTimeResultGroupDefinition_2 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Basic Counters", \
    GroupId="object://customgroup/cded8621-5e71-4a39-afd4-71d9faf37273/Basic Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalBitCount TotalBitCount TotalBitRate TotalBitRate L1BitCount L1BitCount L1BitRate L1BitRate L1BitRatePercent L1BitRatePercent GeneratorFrameCount GeneratorSigFrameCount SigFrameCount TotalFrameRate TotalFrameRate GeneratorFrameRate GeneratorOctetRate GeneratorBitRate GeneratorSigFrameRate SigFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorFrameCount AS 'Generator Count (Frames)', GeneratorPortResults.GeneratorSigFrameCount AS 'Generator Sig Count (Frames)', AnalyzerPortResults.SigFrameCount AS 'Rx Sig Count (Frames)', (GeneratorPortResults.TotalOctetCount * 8) AS 'Total Tx  Count (bits)', (AnalyzerPortResults.TotalOctetCount * 8) AS 'Total Rx Count (bits)', GeneratorPortResults.L1BitCount AS 'Tx L1 Count (bits)', AnalyzerPortResults.L1BitCount AS 'Rx L1 Count (bits)', AnalyzerPortResults.MinFrameLength AS 'Rx Min FrameLength', AnalyzerPortResults.MaxFrameLength AS 'Rx Max FrameLength', GeneratorPortResults.TotalCellCount AS 'Total Tx Count (Cells)', AnalyzerPortResults.TotalCellCount AS 'Total Rx Count (Cells)' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_3 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Errors", \
    GroupId="object://customgroup/e26c15e5-fb73-46ad-a76b-45304a4e6303/Errors", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount FcsErrorFrameCount GeneratorCrcErrorFrameCount GeneratorL3ChecksumErrorCount GeneratorL4ChecksumErrorCount Ipv4ChecksumErrorCount TcpChecksumErrorCount UdpChecksumErrorCount PrbsFillOctetCount PrbsBitErrorCount PrbsBitErrorRatio PrbsErrorFrameCount FcsErrorFrameRate GeneratorCrcErrorFrameRate GeneratorL3ChecksumErrorRate GeneratorL4ChecksumErrorRate Ipv4ChecksumErrorRate TcpChecksumErrorRate UdpChecksumErrorRate PrbsBitErrorRate PrbsErrorFrameRate OutSeqFrameCount", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.FcsErrorFrameCount AS 'Rx FCS Error Count (Frames)', GeneratorPortResults.GeneratorCrcErrorFrameCount AS 'Generator CRC Error Count (Frames)', GeneratorPortResults.GeneratorL3ChecksumErrorCount AS 'Generator L3 Checksum Error Count', GeneratorPortResults.GeneratorL4ChecksumErrorCount AS 'Generator L4 Checksum Error Count', AnalyzerPortResults.Ipv4ChecksumErrorCount AS 'Rx IPv4 Checksum Error Count', AnalyzerPortResults.TcpChecksumErrorCount AS 'Rx TCP Checksum Error Count', AnalyzerPortResults.UdpChecksumErrorCount AS 'Rx UDP Checksum Error Count', AnalyzerPortResults.PrbsFillOctetCount AS 'Rx PRBS Fill Octet Count', AnalyzerPortResults.PrbsBitErrorCount AS 'Rx PRBS Bit Error Count', coalesce(round(cast(AnalyzerPortResults.PrbsBitErrorCount as double)/cast((AnalyzerPortResults.PrbsFillOctetCount * 8) as double), 3), 0.0) as 'PRBS Bit Error Ratio', AnalyzerPortResults.PrbsErrorFrameCount AS 'Rx PRBS Error Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_4 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Triggers", \
    GroupId="object://customgroup/ddcfebff-9e2d-49e4-8d4a-1cde4792f3c1/Triggers", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount Trigger1Count Trigger2Count Trigger3Count Trigger4Count Trigger5Count Trigger6Count Trigger7Count Trigger8Count ComboTriggerCount Trigger1Rate Trigger2Rate Trigger3Rate Trigger4Rate Trigger5Rate Trigger6Rate Trigger7Rate Trigger8Rate ComboTriggerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 40")

    RealTimeResultGroupDefinition_5 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Protocols", \
    GroupId="object://customgroup/3e090a0e-d3c7-413f-ad01-ccb4a21de519/Protocols", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalIpv4FrameCount TotalIpv6FrameCount TotalMplsFrameCount GeneratorIpv4FrameCount GeneratorIpv6FrameCount GeneratorVlanFrameCount GeneratorMplsFrameCount Ipv4FrameCount Ipv6FrameCount TcpFrameCount UdpFrameCount MplsFrameCount IcmpFrameCount VlanFrameCount FcoeFrameCount TotalIpv4FrameRate TotalIpv6FrameRate TotalMplsFrameRate GeneratorIpv4FrameRate GeneratorIpv6FrameRate GeneratorVlanFrameRate GeneratorMplsFrameRate Ipv4FrameRate Ipv6FrameRate TcpFrameRate UdpFrameRate MplsFrameRate IcmpFrameRate VlanFrameRate FcoeFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Frame Count', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Frame Count', GeneratorPortResults.TotalIpv4FrameCount AS 'Total Tx IPv4 Frame', GeneratorPortResults.TotalIpv6FrameCount AS 'Total Tx IPv6 Frame', GeneratorPortResults.TotalMplsFrameCount AS 'Total Tx MPLS Frame', GeneratorPortResults.GeneratorIpv4FrameCount AS 'Generator IPv4 Frame Count', GeneratorPortResults.GeneratorIpv6FrameCount AS 'Generator IPv6 Frame Count', GeneratorPortResults.GeneratorVlanFrameCount AS 'Generator VLAN Frame Count', GeneratorPortResults.GeneratorMplsFrameCount AS 'Generator MPLS Frame Count', AnalyzerPortResults.Ipv4FrameCount AS 'Rx IPv4 Frame Count', AnalyzerPortResults.Ipv6FrameCount AS 'Rx IPv6 Frame Count', AnalyzerPortResults.TcpFrameCount AS 'Rx TCP Frame Count', AnalyzerPortResults.UdpFrameCount AS 'Rx UDP Frame Count', AnalyzerPortResults.MplsFrameCount AS 'Rx MPLS Frame Count', AnalyzerPortResults.IcmpFrameCount AS 'Rx ICMP Frame Count', AnalyzerPortResults.VlanFrameCount AS 'Rx VLAN Frame Count', AnalyzerPortResults.FcoeFrameCount AS 'Rx FCoE Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 41")

    RealTimeResultColumnDefinition_78 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="90", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 88")

    RealTimeResultColumnDefinition_79 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameRate", \
    ColumnDescription="", \
    ColumnWidth="115", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 89")

    RealTimeResultColumnDefinition_80 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 90")

    RealTimeResultColumnDefinition_81 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 91")

    RealTimeResultColumnDefinition_82 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 92")

    RealTimeResultColumnDefinition_83 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="114", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 93")

    RealTimeResultColumnDefinition_84 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 94")

    RealTimeResultColumnDefinition_85 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="77", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 95")

    RealTimeResultColumnDefinition_86 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="84", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 96")

    RealTimeResultColumnDefinition_87 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameRate", \
    ColumnDescription="", \
    ColumnWidth="86", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 97")

    RealTimeResultColumnDefinition_88 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="79", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 98")

    RealTimeResultColumnDefinition_89 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameRate", \
    ColumnDescription="", \
    ColumnWidth="113", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 99")

    RealTimeResultGroupDefinition_6 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Undersize/Oversize/Jumbo", \
    GroupId="object://customgroup/06ce5837-a7ee-427b-96e8-10cca3ff961a/Undersize/Oversize/Jumbo", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount GeneratorUndersizeFrameCount UndersizeFrameCount GeneratorOversizeFrameCount OversizeFrameCount GeneratorJumboFrameCount JumboFrameCount PauseFrameCount GeneratorUndersizeFrameRate UndersizeFrameRate GeneratorOversizeFrameRate OversizeFrameRate GeneratorJumboFrameRate JumboFrameRate PauseFrameRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 8")

    RealTimeResultColumnDefinition_90 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 100")

    RealTimeResultColumnDefinition_91 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 101")

    RealTimeResultColumnDefinition_92 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="200", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 102")

    RealTimeResultColumnDefinition_93 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 103")

    RealTimeResultColumnDefinition_94 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="194", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 104")

    RealTimeResultColumnDefinition_95 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="192", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 613")

    RealTimeResultColumnDefinition_96 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="185", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 614")

    RealTimeResultColumnDefinition_97 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="182", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 615")

    RealTimeResultColumnDefinition_98 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameCount", \
    ColumnDescription="", \
    ColumnWidth="179", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 616")

    RealTimeResultColumnDefinition_99 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="172", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 617")

    RealTimeResultColumnDefinition_100 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 618")

    RealTimeResultColumnDefinition_101 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="166", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 619")

    RealTimeResultColumnDefinition_102 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="129", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 127")

    RealTimeResultColumnDefinition_103 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="191", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 128")

    RealTimeResultColumnDefinition_104 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="119", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 129")

    RealTimeResultColumnDefinition_105 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameRate", \
    ColumnDescription="", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 130")

    RealTimeResultColumnDefinition_106 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="", \
    ColumnWidth="96", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 131")

    RealTimeResultColumnDefinition_107 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 132")

    RealTimeResultColumnDefinition_108 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 133")

    RealTimeResultColumnDefinition_109 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 134")

    RealTimeResultColumnDefinition_110 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 135")

    RealTimeResultColumnDefinition_111 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 136")

    RealTimeResultColumnDefinition_112 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 137")

    RealTimeResultColumnDefinition_113 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 138")

    RealTimeResultColumnDefinition_114 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_115 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_116 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_117 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_118 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_119 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_120 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_121 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_122 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_7 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="PFC Counters", \
    GroupId="object://customgroup/ce2848b9-5f04-419d-8809-030032c630e4/PFC Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount PfcFrameCount PfcFrameRate PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.PfcFrameCount AS 'Tx PFC Count (Frames)', AnalyzerPortResults.PfcFrameCount AS 'Rx PFC Count (Frames)', GeneratorPortResults.PfcPri0FrameCount AS 'Tx PFC Priority0 Count (Frames)', GeneratorPortResults.PfcPri1FrameCount AS 'Tx PFC Priority1 Count (Frames)', GeneratorPortResults.PfcPri2FrameCount AS 'Tx PFC Priority2 Count (Frames)', GeneratorPortResults.PfcPri3FrameCount AS 'Tx PFC Priority3 Count (Frames)', GeneratorPortResults.PfcPri4FrameCount AS 'Tx PFC Priority4 Count (Frames)', GeneratorPortResults.PfcPri5FrameCount AS 'Tx PFC Priority5 Count (Frames)', GeneratorPortResults.PfcPri6FrameCount AS 'Tx PFC Priority6 Count (Frames)', GeneratorPortResults.PfcPri7FrameCount AS 'Tx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0FrameCount AS 'Rx PFC Priority0 Count (Frames)', AnalyzerPortResults.PfcPri1FrameCount AS 'Rx PFC Priority1 Count (Frames)', AnalyzerPortResults.PfcPri2FrameCount AS 'Rx PFC Priority2 Count (Frames)', AnalyzerPortResults.PfcPri3FrameCount AS 'Rx PFC Priority3 Count (Frames)', AnalyzerPortResults.PfcPri4FrameCount AS 'Rx PFC Priority4 Count (Frames)', AnalyzerPortResults.PfcPri5FrameCount AS 'Rx PFC Priority5 Count (Frames)', AnalyzerPortResults.PfcPri6FrameCount AS 'Rx PFC Priority6 Count (Frames)', AnalyzerPortResults.PfcPri7FrameCount AS 'Rx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0Quanta AS 'Rx PFC Priority0 Quanta', AnalyzerPortResults.PfcPri1Quanta AS 'Rx PFC Priority1 Quanta', AnalyzerPortResults.PfcPri2Quanta AS 'Rx PFC Priority2 Quanta', AnalyzerPortResults.PfcPri3Quanta AS 'Rx PFC Priority3 Quanta', AnalyzerPortResults.PfcPri4Quanta AS 'Rx PFC Priority4 Quanta', AnalyzerPortResults.PfcPri5Quanta AS 'Rx PFC Priority5 Quanta', AnalyzerPortResults.PfcPri6Quanta AS 'Rx PFC Priority6 Quanta', AnalyzerPortResults.PfcPri7Quanta AS 'Rx PFC Priority7 Quanta' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_123 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_124 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OutSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_125 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_126 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_127 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_128 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_129 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_130 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_131 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_132 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_133 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_134 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_135 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_136 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_137 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_8 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="User Defined", \
    GroupId="object://customgroup/45684926-5012-4d7b-a560-70e552840cbb/User Defined", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1 UserDefinedFrameRate1 UserDefinedFrameCount2 UserDefinedFrameRate2 UserDefinedFrameCount3 UserDefinedFrameRate3 UserDefinedFrameCount4 UserDefinedFrameRate4 UserDefinedFrameCount5 UserDefinedFrameRate5 UserDefinedFrameCount6 UserDefinedFrameRate6", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.UserDefinedFrameCount1 AS 'User Defined Capture Frame Count 1 (Frames)', AnalyzerPortResults.UserDefinedFrameCount2 AS 'User Defined Capture Frame Count 2 (Frames)', AnalyzerPortResults.UserDefinedFrameCount3 AS 'User Defined Capture Frame Count 3 (Frames)', AnalyzerPortResults.UserDefinedFrameCount4 AS 'User Defined Capture Frame Count 4 (Frames)', AnalyzerPortResults.UserDefinedFrameCount5 AS 'User Defined Capture Frame Count 5 (Frames)', AnalyzerPortResults.UserDefinedFrameCount6 AS 'User Defined Capture Frame Count 6 (Frames)'  FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 14")

    RealTimeResultColumnDefinition_138 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="InOrderFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_139 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ReorderedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_140 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DroppedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_141 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DuplicateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_142 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="LateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_143 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TxQueueFullDropCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_144 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TxQueueFullRetryCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultGroupDefinition_9 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Advanced Sequencing", \
    GroupId="object://customgroup/d775c482-4220-4044-b3d8-d0980146f9dc/Advanced Sequencing", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults", \
    ColumnPropertyName="DroppedFrameCount InOrderFrameCount ReorderedFrameCount DuplicateFrameCount LateFrameCount TxQueueFullDropCount TxQueueFullRetryCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)', GeneratorPortResults.TxQueueFullDropCount AS 'Tx Queue Full Drop Count (Frames)', GeneratorPortResults.TxQueueFullRetryCount AS 'Tx Queue Full Retry Count (Frames)' FROM Port, AnalyzerPortResults, GeneratorPortResults, Analyzer, Generator WHERE ( Analyzer.ParentHnd = Port.Handle AND Generator.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)', GeneratorPortResults.TxQueueFullDropCount AS 'Tx Queue Full Drop Count (Frames)', GeneratorPortResults.TxQueueFullRetryCount AS 'Tx Queue Full Retry Count (Frames)' FROM ExternalDevicePort, AnalyzerPortResults, GeneratorPortResults, Port, Analyzer, Generator WHERE ( Analyzer.ParentHnd = Port.Handle AND Generator.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_145 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_146 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_147 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecSymbols", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_148 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_149 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 148")

    RealTimeResultColumnDefinition_150 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 149")

    RealTimeResultColumnDefinition_151 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 150")

    RealTimeResultColumnDefinition_152 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 151")

    RealTimeResultColumnDefinition_153 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="10", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 152")

    RealTimeResultGroupDefinition_10 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="FEC Counters", \
    GroupId="object://customgroup/bdefbcbd-7034-44a1-9d63-b5a6b6736efb/FEC Counters", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount UncorrectedRsFecErrorCount CorrectedRsFecSymbols CorrectedBaseRFecErrorCount UncorrectedBaseRFecErrorCount PreRsFecSerRate PostRsFecSerRate PreBaseRFecSerRate PostBaseRFecSerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (Frames)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (Frames)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Bits (bits)', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (Frames)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (Frames)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (fps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (fps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (fps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (fps)' FROM Port, AnalyzerPortResults, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (Frames)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (Frames)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Bits (bits)', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (Frames)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (Frames)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (fps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (fps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (fps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (fps)' FROM ExternalDevicePort, AnalyzerPortResults, Port, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 10")

    Perspective_1 = stc.create("Perspective",under = Project_1, \
    PerspectiveViewOwner="SYSTEM", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Perspective 1")

    PerspectiveNode_1 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3", \
    Data="<NodeData Name=\"resultFrame.1\" FrameId=\"8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3\" Active=\"true\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData><NodeContentData FrameName=\"frame://core/Port/ResultQuery:(1, 0, 0)\" ResultDataSetId=\"Port Traffic\\Basic Traffic Results\" Column=\"0\" Row=\"0\" DockPanelNumber=\"1\" /><NodeContentData FrameName=\"frame://core/DynamicResultView/ResultQuery:(1, 0, 1)\" ResultDataSetId=\"Port Traffic and Counters\\Aggregate Port L1 Tx Rate\" Column=\"1\" Row=\"0\" DockPanelNumber=\"1\" /></ContentData> 
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 1")

    PerspectiveNode_2 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="1F412EE6-760C-4937-9644-ACFA463EA44E", \
    Data="<NodeData Name=\"resultFrame.2\" FrameId=\"1F412EE6-760C-4937-9644-ACFA463EA44E\" Active=\"false\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData /> 
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 2")

    DynamicResultView_1 = stc.create("DynamicResultView",under = Project_1, \
    ResultSourceClass="Port", \
    SaveToConfig="TRUE", \
    Identifier="Port Traffic and Counters\\Aggregate Port L1 Tx Rate", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/DynamicResultView", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Aggregate Port L1 Tx Rate")

    PresentationResultQuery_1 = stc.create("PresentationResultQuery",under = DynamicResultView_1, \
    SelectProperties="Port.TxL1BitRate Port.TxMaxLineRate Project.Name", \
    WhereConditions="", \
    GroupByProperties="Project.Name", \
    LimitOffset="0", \
    LimitSize="2000", \
    SortBy="", \
    ArchivingOption="NONE", \
    ResultState="IDLE", \
    ArchivingInterval="10", \
    DatabaseFileName="", \
    DisableAutoGrouping="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PresentationResultQuery 1")

    ColumnDisplayProperties_1 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxL1BitRate", \
    ColumnCaption="Tx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 1")

    ColumnDisplayProperties_2 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxMaxLineRate", \
    ColumnCaption="Tx Max Line Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 2")

    ColumnDisplayProperties_3 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Project.Name", \
    ColumnCaption="Project Name", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 3")

    AutomationOptions_1 = (stc.get( system1, 'children-AutomationOptions' )).split(' ')[0]
    stc.config(AutomationOptions_1, \
    CommandTimeout="3600", \
    LogLevel="WARN", \
    LogTo="stdout", \
    MaxBackup="0", \
    MaxFileSizeInMB="10", \
    SuppressTclErrors="FALSE", \
    AutoSubscribe="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutomationOptions 1")

    PhysicalChassisManager_1 = stc.create("PhysicalChassisManager",under = system1, \
    RawImageArchiveDir="", \
    FirmwareArchiveDir="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhysicalChassisManager 1")

    Sequencer_1 = stc.create("Sequencer",under = system1, \
    CurrentSubCommandName="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Sequencer")

    SequencerGroupCommand_1 = stc.create("SequencerGroupCommand",under = system1, \
    ExecutionMode="BACKGROUND", \
    GroupCategory="CLEANUP_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Cleanup Commands")

    IfManager_1 = stc.create("IfManager",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IfManager 1")

    LinkRegistry_1 = stc.create("LinkRegistry",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LinkRegistry 1")

    FeatureSupportedVersion_1 = (stc.get( system1, 'children-FeatureSupportedVersion' )).split(' ')[0]
    stc.config(FeatureSupportedVersion_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FeatureSupportedVersion 1")

    ActiveEventManager_1 = (stc.get( system1, 'children-ActiveEventManager' )).split(' ')[0]
    stc.config(ActiveEventManager_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ActiveEventManager 1")

    spirent_results_EnhancedResultsSelectorProfile_1 = stc.create("spirent.results.EnhancedResultsSelectorProfile",under = system1, \
    SubscribeType="SELECTED", \
    ConfigSubscribeType="SELECTED", \
    EnableLiveDataRetention="TRUE", \
    LiveDataRetentionInterval="15", \
    StorageLimitInKB="-1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsSelectorProfile 1")

    spirent_results_EnhancedResultsGroupFilter_1 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="autosartimesync_can_stats", \
    LiveFacts="state rx_bad_crc_count rx_follow_up_count rx_lost_follow_up_count rx_lost_sync_count rx_ovs rx_sgw rx_sync_count rx_avg_time_between_syncs rx_current_time_between_syncs_and_followup rx_current_time_between_sync rx_long_avg_time_between_syncs rx_max_time_between_syncs rx_min_time_between_syncs rx_short_avg_time_between_syncs rx_time_domain time_of_day time_of_day_seconds tx_follow_up_count tx_sync_count rx_ovs_set_count rx_sgw_bit_count rx_avg_time_between_syncs_and_followup rx_max_time_between_syncs_and_followup rx_min_time_between_syncs_and_followup rx_invalid_follow_up_count rx_invalid_sync_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 10")

    spirent_results_EnhancedResultsGroupFilter_2 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_afi_safi_stats", \
    LiveFacts="rx_advertised_route_count rx_withdrawn_route_count session_count tx_advertised_route_count tx_withdrawn_route_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 11")

    spirent_results_EnhancedResultsGroupFilter_3 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_ls_scale_stats", \
    LiveFacts="tx_advertised_ls_scale_link_route_count tx_advertised_ls_scale_node_route_count tx_advertised_ls_scale_prefix_ipv4_route_count tx_withdrawn_ls_scale_node_route_count tx_withdrawn_ls_scale_link_route_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 12")

    spirent_results_EnhancedResultsGroupFilter_4 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bgp_session_stats", \
    LiveFacts="last_rx_update_route_count outstanding_route_count state rx_advertised_evpn_ad_route_count rx_advertised_evpn_eth_segment_route_count rx_advertised_evpn_mcast_route_count rx_advertised_evpn_ip_prefix_route_count rx_advertised_evpn_join_synch_route_count rx_advertised_evpn_leave_synch_route_count rx_advertised_evpn_mac_route_count rx_advertised_evpn_selective_mcast_route_count rx_advertised_route_count rx_advertised_update_count rx_keepalive_count rx_notification_count rx_notify_code rx_notify_sub_code rx_open_count rx_route_refresh_count rx_rt_constraint_count rx_withdrawn_evpn_ad_route_count rx_withdrawn_evpn_eth_segment_route_count rx_withdrawn_evpn_mcast_route_count rx_withdrawn_evpn_ip_prefix_route_count rx_withdrawn_evpn_join_synch_route_count rx_withdrawn_evpn_leave_synch_route_count rx_withdrawn_evpn_mac_route_count rx_withdrawn_evpn_selective_mcast_route_count rx_withdrawn_route_count session_up_count tx_advertised_evpn_ad_route_count tx_advertised_evpn_eth_segment_route_count tx_advertised_evpn_mcast_route_count tx_advertised_evpn_ip_prefix_route_count tx_advertised_evpn_join_synch_route_count tx_advertised_evpn_leave_synch_route_count tx_advertised_evpn_mac_route_count tx_advertised_evpn_selective_mcast_route_count tx_advertised_route_count tx_advertised_update_count tx_keepalive_count tx_notification_count tx_notify_code tx_notify_sub_code tx_open_count tx_route_refresh_count tx_rt_constraint_count tx_withdrawn_evpn_ad_route_count tx_withdrawn_evpn_eth_segment_route_count tx_withdrawn_evpn_mcast_route_count tx_withdrawn_evpn_ip_prefix_route_count tx_withdrawn_evpn_join_synch_route_count tx_withdrawn_evpn_leave_synch_route_count tx_withdrawn_evpn_mac_route_count tx_withdrawn_evpn_selective_mcast_route_count tx_withdrawn_route_count tx_withdrawn_update_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 13")

    spirent_results_EnhancedResultsGroupFilter_5 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="dhcpv4_block_stats", \
    LiveFacts="currently_engaged currently_bound currently_idle state total_bound total_failed total_renewed ack_rx decline_tx discover_tx dna_failed_tx dna_reply_rx dna_req_tx dna_retry_tx force_renew_rx garp_rx garp_tx reboot_tx nak_rx offer_rx rebind_tx release_tx renew_tx request_retry_tx request_tx total_discover_retry_tx attempt_rate bind_rate connect_start_time current_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 14")

    spirent_results_EnhancedResultsGroupFilter_6 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="dhcpv6_block_stats", \
    LiveFacts="currently_engaged currently_bound currently_idle state total_bound total_declined total_failed total_rebound total_released total_renewed pd_state advertise_rx confirm_tx decline_tx info_request_tx rebind_tx release_tx renew_tx request_tx solicit_tx total_release_retry_tx total_renew_retry_tx total_solicit_retry_tx reconfigure_rx reply_rx attempt_rate bind_rate rebind_rate release_rate renew_rate connect_start_time current_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 15")

    spirent_results_EnhancedResultsGroupFilter_7 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ecpri_device_stats", \
    LiveFacts="state rx_followup_count rx_remote_request_count rx_remote_request_with_fu_count rx_request_count rx_request_with_fu_count rx_response_count tx_followup_count tx_remote_request_count tx_remote_request_with_fu_count tx_request_count tx_request_with_fu_count tx_response_count rx_remote_reset_request_count rx_remote_reset_response_count tx_remote_reset_request_count tx_remote_reset_response_count rx_type4_failure_read_response_count rx_type4_failure_write_response_count rx_type4_partial_read_response_count rx_type4_partial_write_response_count rx_type4_read_request_count rx_type4_read_response_count rx_type4_write_no_response_count rx_type4_write_request_count rx_type4_write_response_count tx_type4_failure_read_response_count tx_type4_failure_write_response_count tx_type4_partial_read_response_count tx_type4_partial_write_response_count tx_type4_read_request_count tx_type4_read_response_count tx_type4_write_no_response_count tx_type4_write_request_count tx_type4_write_response_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 16")

    spirent_results_EnhancedResultsGroupFilter_8 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee1588v2_clock_stats", \
    LiveFacts="clock_domain clock_state port_number rx_announce_count rx_delay_request_count rx_delay_response_count rx_follow_up_count rx_peer_delay_request_count rx_peer_delay_response_count rx_peer_delay_response_follow_up_count rx_signaling_count rx_sync_count tx_announce_count tx_delay_request_count tx_delay_response_count tx_follow_up_count tx_peer_delay_request_count tx_peer_delay_response_count tx_peer_delay_response_follow_up_count tx_signaling_count tx_sync_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 17")

    spirent_results_EnhancedResultsGroupFilter_9 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee1588v2_clock_sync_stats", \
    LiveFacts="follow_up_correction_field pdelay_response_correction_field pdelay_response_followup_correction_field sync_correction_field invalid_timestamp_count average_mean_path_delay current_mean_path_delay max_mean_path_delay min_mean_path_delay peer_mean_path_delay log_min_delay_request_interval step_removed average_offset_minus_deviation average_offset_plus_deviation current_offset negative_offset_peak offset_deviation offset_standard_deviation positive_offset_peak t1_in_nano_seconds t2_in_nano_seconds t3_in_nano_seconds t4_in_nano_seconds time_of_day time_of_day_in_nano_seconds", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 18")

    spirent_results_EnhancedResultsGroupFilter_10 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_client_stats", \
    LiveFacts="authentication_type channel_number channel_width state reason_code ft_ave_delay ft_delay ft_fail ft_max_delay ft_min_delay ft_success ft_type freq_band group_id wlan_mode mfp_status mimo_mode noise_floor rx_guard_interval rx_mcs_type rx_nss rx_rate signal_strength startup_time sta_state sumu tdls_peer_status time_in_association rx_bytes rx_packets tx_bytes tx_packets guard_interval mcs_type tx_nss tx_rate wmm_status per_chn_width_rx_pkts_3 per_chn_width_rx_pkts_0 per_chn_width_rx_pkts_1 per_chn_width_rx_pkts_2 per_chn_width_tx_pkts_3 per_chn_width_tx_pkts_0 per_chn_width_tx_pkts_1 per_chn_width_tx_pkts_2 per_gi_rx_pkts_1600ns_0 per_gi_rx_pkts_1600ns_1 per_gi_rx_pkts_1600ns_10 per_gi_rx_pkts_1600ns_11 per_gi_rx_pkts_1600ns_2 per_gi_rx_pkts_1600ns_3 per_gi_rx_pkts_1600ns_4 per_gi_rx_pkts_1600ns_5 per_gi_rx_pkts_1600ns_6 per_gi_rx_pkts_1600ns_7 per_gi_rx_pkts_1600ns_8 per_gi_rx_pkts_1600ns_9 per_gi_rx_pkts_3200ns_0 per_gi_rx_pkts_3200ns_1 per_gi_rx_pkts_3200ns_10 per_gi_rx_pkts_3200ns_11 per_gi_rx_pkts_3200ns_2 per_gi_rx_pkts_3200ns_3 per_gi_rx_pkts_3200ns_4 per_gi_rx_pkts_3200ns_5 per_gi_rx_pkts_3200ns_6 per_gi_rx_pkts_3200ns_7 per_gi_rx_pkts_3200ns_8 per_gi_rx_pkts_3200ns_9 per_gi_rx_pkts_400ns_0 per_gi_rx_pkts_400ns_1 per_gi_rx_pkts_400ns_10 per_gi_rx_pkts_400ns_11 per_gi_rx_pkts_400ns_2 per_gi_rx_pkts_400ns_3 per_gi_rx_pkts_400ns_4 per_gi_rx_pkts_400ns_5 per_gi_rx_pkts_400ns_6 per_gi_rx_pkts_400ns_7 per_gi_rx_pkts_400ns_8 per_gi_rx_pkts_400ns_9 per_gi_rx_pkts_800ns_0 per_gi_rx_pkts_800ns_1 per_gi_rx_pkts_800ns_10 per_gi_rx_pkts_800ns_11 per_gi_rx_pkts_800ns_2 per_gi_rx_pkts_800ns_3 per_gi_rx_pkts_800ns_4 per_gi_rx_pkts_800ns_5 per_gi_rx_pkts_800ns_6 per_gi_rx_pkts_800ns_7 per_gi_rx_pkts_800ns_8 per_gi_rx_pkts_800ns_9 per_gi_tx_pkts_1600ns_0 per_gi_tx_pkts_1600ns_1 per_gi_tx_pkts_1600ns_10 per_gi_tx_pkts_1600ns_11 per_gi_tx_pkts_1600ns_2 per_gi_tx_pkts_1600ns_3 per_gi_tx_pkts_1600ns_4 per_gi_tx_pkts_1600ns_5 per_gi_tx_pkts_1600ns_6 per_gi_tx_pkts_1600ns_7 per_gi_tx_pkts_1600ns_8 per_gi_tx_pkts_1600ns_9 per_gi_tx_pkts_3200ns_0 per_gi_tx_pkts_3200ns_1 per_gi_tx_pkts_3200ns_10 per_gi_tx_pkts_3200ns_11 per_gi_tx_pkts_3200ns_2 per_gi_tx_pkts_3200ns_3 per_gi_tx_pkts_3200ns_4 per_gi_tx_pkts_3200ns_5 per_gi_tx_pkts_3200ns_6 per_gi_tx_pkts_3200ns_7 per_gi_tx_pkts_3200ns_8 per_gi_tx_pkts_3200ns_9 per_gi_tx_pkts_400ns_0 per_gi_tx_pkts_400ns_1 per_gi_tx_pkts_400ns_10 per_gi_tx_pkts_400ns_11 per_gi_tx_pkts_400ns_2 per_gi_tx_pkts_400ns_3 per_gi_tx_pkts_400ns_4 per_gi_tx_pkts_400ns_5 per_gi_tx_pkts_400ns_6 per_gi_tx_pkts_400ns_7 per_gi_tx_pkts_400ns_8 per_gi_tx_pkts_400ns_9 per_gi_tx_pkts_800ns_0 per_gi_tx_pkts_800ns_1 per_gi_tx_pkts_800ns_10 per_gi_tx_pkts_800ns_11 per_gi_tx_pkts_800ns_2 per_gi_tx_pkts_800ns_3 per_gi_tx_pkts_800ns_4 per_gi_tx_pkts_800ns_5 per_gi_tx_pkts_800ns_6 per_gi_tx_pkts_800ns_7 per_gi_tx_pkts_800ns_8 per_gi_tx_pkts_800ns_9 per_mcs_rx_pkts_0 per_mcs_rx_pkts_1 per_mcs_rx_pkts_10 per_mcs_rx_pkts_11 per_mcs_rx_pkts_2 per_mcs_rx_pkts_3 per_mcs_rx_pkts_4 per_mcs_rx_pkts_5 per_mcs_rx_pkts_6 per_mcs_rx_pkts_7 per_mcs_rx_pkts_8 per_mcs_rx_pkts_9 per_mcs_rx_mu_pkts_0 per_mcs_rx_mu_pkts_1 per_mcs_rx_mu_pkts_10 per_mcs_rx_mu_pkts_11 per_mcs_rx_mu_pkts_2 per_mcs_rx_mu_pkts_3 per_mcs_rx_mu_pkts_4 per_mcs_rx_mu_pkts_5 per_mcs_rx_mu_pkts_6 per_mcs_rx_mu_pkts_7 per_mcs_rx_mu_pkts_8 per_mcs_rx_mu_pkts_9 per_mcs_rx_su_pkts_0 per_mcs_rx_su_pkts_1 per_mcs_rx_su_pkts_10 per_mcs_rx_su_pkts_11 per_mcs_rx_su_pkts_2 per_mcs_rx_su_pkts_3 per_mcs_rx_su_pkts_4 per_mcs_rx_su_pkts_5 per_mcs_rx_su_pkts_6 per_mcs_rx_su_pkts_7 per_mcs_rx_su_pkts_8 per_mcs_rx_su_pkts_9 per_mcs_tx_pkts_0 per_mcs_tx_pkts_1 per_mcs_tx_pkts_10 per_mcs_tx_pkts_11 per_mcs_tx_pkts_2 per_mcs_tx_pkts_3 per_mcs_tx_pkts_4 per_mcs_tx_pkts_5 per_mcs_tx_pkts_6 per_mcs_tx_pkts_7 per_mcs_tx_pkts_8 per_mcs_tx_pkts_9 per_mcs_tx_mu_pkts_0 per_mcs_tx_mu_pkts_1 per_mcs_tx_mu_pkts_10 per_mcs_tx_mu_pkts_11 per_mcs_tx_mu_pkts_2 per_mcs_tx_mu_pkts_3 per_mcs_tx_mu_pkts_4 per_mcs_tx_mu_pkts_5 per_mcs_tx_mu_pkts_6 per_mcs_tx_mu_pkts_7 per_mcs_tx_mu_pkts_8 per_mcs_tx_mu_pkts_9 per_mcs_tx_su_pkts_0 per_mcs_tx_su_pkts_1 per_mcs_tx_su_pkts_10 per_mcs_tx_su_pkts_11 per_mcs_tx_su_pkts_2 per_mcs_tx_su_pkts_3 per_mcs_tx_su_pkts_4 per_mcs_tx_su_pkts_5 per_mcs_tx_su_pkts_6 per_mcs_tx_su_pkts_7 per_mcs_tx_su_pkts_8 per_mcs_tx_su_pkts_9 per_stream_rssi_chw160m_0 per_stream_rssi_chw160m_1 per_stream_rssi_chw160m_2 per_stream_rssi_chw160m_3 per_stream_rssi_chw160m_4 per_stream_rssi_chw160m_5 per_stream_rssi_chw160m_6 per_stream_rssi_chw160m_7 per_stream_rssi_chw20m_0 per_stream_rssi_chw20m_1 per_stream_rssi_chw20m_2 per_stream_rssi_chw20m_3 per_stream_rssi_chw20m_4 per_stream_rssi_chw20m_5 per_stream_rssi_chw20m_6 per_stream_rssi_chw20m_7 per_stream_rssi_chw40m_0 per_stream_rssi_chw40m_1 per_stream_rssi_chw40m_2 per_stream_rssi_chw40m_3 per_stream_rssi_chw40m_4 per_stream_rssi_chw40m_5 per_stream_rssi_chw40m_6 per_stream_rssi_chw40m_7 per_stream_rssi_chw80m_0 per_stream_rssi_chw80m_1 per_stream_rssi_chw80m_2 per_stream_rssi_chw80m_3 per_stream_rssi_chw80m_4 per_stream_rssi_chw80m_5 per_stream_rssi_chw80m_6 per_stream_rssi_chw80m_7 per_stream_rx_pkts_0 per_stream_rx_pkts_1 per_stream_rx_pkts_2 per_stream_rx_pkts_3 per_stream_rx_pkts_4 per_stream_rx_pkts_5 per_stream_rx_pkts_6 per_stream_rx_pkts_7 per_stream_tx_pkts_0 per_stream_tx_pkts_1 per_stream_tx_pkts_2 per_stream_tx_pkts_3 per_stream_tx_pkts_4 per_stream_tx_pkts_5 per_stream_tx_pkts_6 per_stream_tx_pkts_7 rx_ofdma_mode tx_ofdma_mode rx_ru_high_index rx_ru_low_index rx_ofdma_pkts rx_ru_index rx_ru_type tx_ru_high_index tx_ru_low_index tx_ofdma_pkts tx_ru_index tx_ru_type authentication_type_enum_numeric bss_collision_counter channel_width_enum_numeric reason_code_enum_numeric ft_type_enum_numeric freq_band_enum_numeric state_enum_numeric wlan_mode_enum_numeric mfp_status_enum_numeric mimo_mode_enum_numeric rx_guard_interval_enum_numeric rx_mcs_type_enum_numeric rx_mu_packets rx_ppdu_type rx_ppdu_type_enum_numeric rx_su_packets sumu_enum_numeric tdls_peer_status_enum_numeric guard_interval_enum_numeric mcs_type_enum_numeric tx_mu_packets tx_ppdu_type tx_ppdu_type_enum_numeric tx_su_packets wmm_status_enum_numeric rx_pkt_cnt_ru106 rx_pkt_cnt_ru242 rx_pkt_cnt_ru26 rx_pkt_cnt_ru484 rx_pkt_cnt_ru52 rx_pkt_cnt_ru996 rx_ru_type_enum_numeric tx_ru_type_enum_numeric tx_pkt_cnt_ru106 tx_pkt_cnt_ru242 tx_pkt_cnt_ru26 tx_pkt_cnt_ru484 tx_pkt_cnt_ru52 tx_pkt_cnt_ru996", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 19")

    spirent_results_EnhancedResultsGroupFilter_11 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee8021as_clock_sync_stats", \
    LiveFacts="as_capable as_capable_across_domain follow_up_correction_field pdelay_response_correction_field pdelay_response_followup_correction_field sync_correction_field invalid_timestamp_count average_mean_path_delay current_mean_path_delay max_mean_path_delay min_mean_path_delay peer_mean_path_delay log_min_delay_request_interval log_min_pdelay_request_interval step_removed average_offset_minus_deviation average_offset_plus_deviation current_offset negative_offset_peak offset_deviation offset_standard_deviation positive_offset_peak time_of_day time_of_day_in_seconds", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 20")

    spirent_results_EnhancedResultsGroupFilter_12 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="igmp_device_stats", \
    LiveFacts="host_state rx_frame_count rx_unknown_type_count tx_frame_count rx_checksum_error_count rx_length_error_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 21")

    spirent_results_EnhancedResultsGroupFilter_13 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="igmp_host_group_stats", \
    LiveFacts="duplicate_join join_fail join_latency join_timestamp leave_latency leave_timestamp state state_change_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 22")

    spirent_results_EnhancedResultsGroupFilter_14 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="isis_router_stats", \
    LiveFacts="adjacency_level adjacency_three_way_state l1_broadcast_adjacency_state l2_broadcast_adjacency_state state rx_adj_sid_tlv_count rx_backup_adj_sid_tlv_count rx_backup_lan_adj_sid_tlv_count rx_l1_csnp_count rx_l1_lan_hello_count rx_l1_lsp_count rx_l1_psnp_count rx_l2_bundle_adj_sid_tlv_count rx_l2_bundle_lan_adj_sid_tlv_count rx_l2_csnp_count rx_l2_lan_hello_count rx_l2_lsp_count rx_l2_psnp_count rx_lan_adj_sid_tlv_count rx_prefix_sid_tlv_count rx_ptp_hello_count rx_sid_label_binding_tlv_count rx_srlg_tlv_count rx_srv6_capabilities_tlv_count rx_srv6_endx_sid_tlv_count rx_srv6_lan_endx_sid_tlv_count rx_srv6_locator_tlv_count rx_unknown_sid_label_binding_tlv_count tx_adj_sid_tlv_count tx_backup_adj_sid_tlv_count tx_backup_lan_adj_sid_tlv_count tx_l1_csnp_count tx_l1_lan_hello_count tx_l1_lsp_count tx_l1_psnp_count tx_l2_bundle_adj_sid_tlv_count tx_l2_bundle_lan_adj_sid_tlv_count tx_l2_csnp_count tx_l2_lan_hello_count tx_l2_lsp_count tx_l2_psnp_count tx_lan_adj_sid_tlv_count tx_prefix_sid_tlv_count tx_ptp_hello_count tx_sid_label_binding_tlv_count tx_srlg_tlv_count tx_srv6_capabilities_tlv_count tx_srv6_endx_sid_tlv_count tx_srv6_lan_endx_sid_tlv_count tx_srv6_locator_tlv_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 23")

    spirent_results_EnhancedResultsGroupFilter_15 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_port_basic_stats", \
    LiveFacts="first_arrival_time last_arrival_time dropped_frame_count duplicate_frame_count in_order_frame_count late_frame_count out_seq_frame_count preamble_max_length preamble_min_length preamble_total_bytes reordered_frame_count hw_frame_count l1_bit_count l1_bit_rate pause_frame_count pause_frame_rate prbs_fill_octet_count prbs_fill_octet_rate sig_frame_count sig_frame_rate total_octet_count total_cell_count total_frame_count total_octet_rate total_cell_rate total_frame_rate corrected_base_rs_fec_error_count corrected_rs_fec_error_count fcs_error_frame_count fcs_error_frame_rate ipv4_checksum_error_count ipv4_checksum_error_rate jumbo_frame_count jumbo_frame_rate oversize_frame_count oversize_frame_rate prbs_bit_error_count prbs_bit_error_rate prbs_error_frame_count prbs_error_frame_rate tcp_checksum_error_count tcp_checksum_error_rate udp_checksum_error_count udp_checksum_error_rate undersize_frame_count undersize_frame_rate uncorrected_base_rs_fec_error_count uncorrected_rs_fec_error_count corrected_rs_fec_symbols post_base_rs_fec_ser_rate post_rs_fec_ser_rate pre_base_rs_fec_ser_rate pre_rs_fec_ser_rate max_frame_length min_frame_length avg_latency max_latency min_latency pfc_frame_count pfc_pri0_frame_count pfc_pri0_quanta pfc_pri0_frame_rate pfc_pri1_frame_count pfc_pri1_quanta pfc_pri1_frame_rate pfc_pri2_frame_count pfc_pri2_quanta pfc_pri2_frame_rate pfc_pri3_frame_count pfc_pri3_quanta pfc_pri3_frame_rate pfc_pri4_frame_count pfc_pri4_quanta pfc_pri4_frame_rate pfc_pri5_frame_count pfc_pri5_quanta pfc_pri5_frame_rate pfc_pri6_frame_count pfc_pri6_quanta pfc_pri6_frame_rate pfc_pri7_frame_count pfc_pri7_quanta pfc_pri7_frame_rate pfc_frame_rate fcoe_frame_count fcoe_frame_rate icmp_frame_count icmp_frame_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_over_ipv4_frame_count ipv6_over_ipv4_frame_rate ipv6_frame_rate mpls_frame_count mpls_frame_rate tcp_frame_count tcp_frame_rate udp_frame_count udp_frame_rate vlan_frame_count vlan_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 24")

    spirent_results_EnhancedResultsGroupFilter_16 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_port_basic_stats", \
    LiveFacts="generator_octet_count generator_frame_count generator_octet_rate generator_frame_rate generator_sig_frame_count generator_sig_frame_rate total_octet_count total_cell_count total_frame_count total_octet_rate total_cell_rate total_frame_rate hw_frame_count l1_bit_count l1_bit_rate generator_abort_frame_count generator_abort_frame_rate generator_crc_error_frame_count generator_crc_error_frame_rate generator_jumbo_frame_count generator_jumbo_frame_rate generator_l3_checksum_error_count generator_l3_checksum_error_rate generator_l4_checksum_error_count generator_l4_checksum_error_rate generator_oversize_frame_count generator_oversize_frame_rate generator_undersize_frame_count generator_undersize_frame_rate pfc_frame_count pfc_pri0_frame_count pfc_pri1_frame_count pfc_pri2_frame_count pfc_pri3_frame_count pfc_pri4_frame_count pfc_pri5_frame_count pfc_pri6_frame_count pfc_pri7_frame_count generator_ipv4_frame_count generator_ipv4_frame_rate generator_ipv6_frame_count generator_ipv6_frame_rate generator_mpls_frame_count generator_mpls_frame_rate generator_vlan_frame_count generator_vlan_frame_rate total_mpls_frame_rate total_ipv4_frame_count total_ipv4_frame_rate total_ipv6_frame_count total_ipv6_frame_rate total_mpls_frame_count queue_full_drop_count queue_full_retry_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 25")

    spirent_results_EnhancedResultsGroupFilter_17 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_port_cpu_stats", \
    LiveFacts="octet_count frame_count dropped_frame_count dropped_frame_rate neighbor_advertisement_count neighbor_advertisement_rate neighbor_solicitation_count neighbor_solicitation_rate octet_rate frame_rate arp_reply_count arp_reply_rate arp_request_count arp_request_rate icmp_echo_reply_count icmp_echo_reply_rate icmp_echo_request_count icmp_echo_request_rate icmpv6_echo_reply_count icmpv6_echo_reply_rate icmpv6_echo_request_count icmpv6_echo_request_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_frame_rate mpls_frame_count mpls_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 26")

    spirent_results_EnhancedResultsGroupFilter_18 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_port_cpu_stats", \
    LiveFacts="octet_count frame_count neighbor_advertisement_count neighbor_advertisement_rate neighbor_solicitation_count neighbor_solicitation_rate octet_rate frame_rate arp_reply_count arp_reply_rate arp_request_count arp_request_rate icmp_echo_reply_count icmp_echo_reply_rate icmp_echo_request_count icmp_echo_request_rate icmpv6_echo_reply_count icmpv6_echo_reply_rate icmpv6_echo_request_count icmpv6_echo_request_rate ipv4_frame_count ipv4_frame_rate ipv6_frame_count ipv6_frame_rate mpls_frame_count mpls_frame_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 27")

    spirent_results_EnhancedResultsGroupFilter_19 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rx_stream_stats", \
    LiveFacts="first_arrival_time last_arrival_time max_interarrival_time min_interarrival_time total_interarrival_time dropped_frame_count dropped_frame_rate duplicate_frame_count duplicate_frame_rate in_seq_frame_count in_seq_frame_rate in_order_frame_count in_order_frame_rate late_frame_count late_frame_rate out_seq_frame_count out_seq_frame_rate prbs_fill_octet_count prbs_fill_octet_rate reordered_frame_count reordered_frame_rate octet_count cell_count frame_count l1_bit_count l1_bit_rate octet_rate cell_rate frame_rate sig_frame_count sig_frame_rate prbs_bit_error_count prbs_error_frame_count prbs_error_frame_rate prbs_bit_error_rate fcs_error_frame_count fcs_error_frame_rate ipv4_checksum_error_count ipv4_checksum_error_rate tcp_udp_checksum_error_count tcp_udp_checksum_error_rate max_jitter min_jitter total_jitter total_jitter_rate max_latency min_latency total_latency expected_seq_num last_seq_num seq_run_length counter_timestamp avg_jitter avg_latency hist_bin1_count hist_bin10_count hist_bin11_count hist_bin12_count hist_bin13_count hist_bin14_count hist_bin15_count hist_bin16_count hist_bin2_count hist_bin3_count hist_bin4_count hist_bin5_count hist_bin6_count hist_bin7_count hist_bin8_count hist_bin9_count short_term_avg_latency", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 28")

    spirent_results_EnhancedResultsGroupFilter_20 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="tx_stream_stats", \
    LiveFacts="octet_count cell_count frame_count l1_bit_count l1_bit_rate octet_rate cell_rate frame_rate counter_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 29")

    spirent_results_EnhancedResultsGroupFilter_21 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pim_router_stats", \
    LiveFacts="mdt_join_count neighbor_count state rx_group_rp_count rx_group_starg_count rx_group_sg_count rx_group_sgrpt_count rx_assert_count rx_bootstrap_count rx_hello_count rx_joinprune_count rx_register_count rx_register_stop_count tx_group_rp_count tx_group_starg_count tx_group_sg_count tx_group_sgrpt_count tx_bootstrap_count tx_hello_count tx_joinprune_count tx_register_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 30")

    spirent_results_EnhancedResultsGroupFilter_22 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ppp_block_stats", \
    LiveFacts="block_state ipv4cp_block_state ipv6cp_block_state attempted sessions succ_disc failed_disc failed_conn succ_conn sessions_up retry avg_succ_tx chap_rx chap_tx ipcp_rx ipcp_tx ipv6cp_rx ipv6cp_tx lcp_conf_ack_rx lcp_conf_ack_tx lcp_conf_nak_rx lcp_conf_nak_tx lcp_conf_rej_rx lcp_conf_rej_tx lcp_conf_req_rx lcp_conf_req_tx lcp_echo_rep_rx lcp_echo_rep_tx lcp_echo_req_rx lcp_echo_req_tx lcp_term_ack_rx lcp_term_ack_tx lcp_term_req_rx lcp_term_req_tx padi_rx padi_tx pado_rx pado_tx padr_rx padr_tx pads_rx pads_tx padt_rx padt_tx pap_rx pap_tx succ_setup_rate max_setup_time min_setup_time avg_setup_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 31")

    spirent_results_EnhancedResultsGroupFilter_23 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="roe_block_stats", \
    LiveFacts="state rx_cpri_port_tlv_count rx_demapper_container_tlv_count rx_demapper_fft_tlv_count rx_demapper_tlv_count rx_ethernet_link_tlv_count rx_frame_count rx_roe_19141_tlv_count rx_mapper_container_tlv_count rx_mapper_fft_tlv_count rx_mapper_prach_tlv_count rx_mapper_tlv_count rx_dropped_count rx_dropped_rate tx_cpri_port_tlv_count tx_demapper_container_tlv_count tx_demapper_fft_tlv_count tx_demapper_tlv_count tx_ethernet_link_tlv_count tx_frame_count tx_roe_19141_tlv_count tx_mapper_container_tlv_count tx_mapper_fft_tlv_count tx_mapper_prach_tlv_count tx_mapper_tlv_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 32")

    spirent_results_EnhancedResultsGroupFilter_24 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="rsvp_te_stats", \
    LiveFacts="avg_lsp_setup_time egress_lsp_up_count last_rx_path_error_code last_rx_resv_error_code last_tx_path_error_code last_tx_resv_error_code lsp_connecting_count lsp_down_count lsp_up_count max_lsp_setup_time min_lsp_setup_time state rx_hello rx_notify rx_path rx_path_error rx_path_recovery rx_path_tear rx_resv rx_resv_confirm rx_resv_error rx_resv_tear tx_hello tx_notify tx_path tx_path_error tx_path_recovery tx_path_tear tx_resv tx_resv_confirm tx_resv_error tx_resv_tear", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 33")

    spirent_results_EnhancedResultsGroupFilter_25 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ecpri_type_5_message_stats", \
    LiveFacts="measurement_id avg_delay max_delay min_delay rx_follow_up_count rx_remote_request_count rx_remote_request_with_follow_up_count rx_request_count rx_request_with_follow_up_count rx_response_count tx_follow_up_count tx_remote_request_count tx_remote_request_with_follow_up_count tx_request_count tx_request_with_follow_up_count tx_response_count curr_delay", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 25")

    spirent_results_EnhancedResultsConfigSelection_1 = stc.create("spirent.results.EnhancedResultsConfigSelection",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    DimensionSetName="tx_stream_config", \
    PropertyList="frames_per_second", \
    EnableAuto="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsConfigSelection 1")

    spirent_results_EnhancedResultsGroupFilter_26 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="bfd_session_stats", \
    LiveFacts="bfd_diagnostic_code flaps_detected last_bfd_diagnostic_error_rx my_discriminator state rx_bfd_packets sessions_down sessions_up timesouts_detected tx_bfd_packets your_discriminator", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 45")

    spirent_results_EnhancedResultsGroupFilter_27 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ospfv2_session_stats", \
    LiveFacts="adjacency_status area_id ipv4_src_address state session_up_count rx_ack rx_as_external_lsa rx_asbr_summary_lsa rx_dd rx_el_lsa rx_ep_lsa rx_hello rx_network_lsa rx_nssa_lsa rx_request rx_ri_lsa rx_router_lsa rx_summary_lsa rx_te_lsa tx_ack tx_as_external_lsa tx_asbr_summary_lsa tx_dd tx_el_lsa tx_ep_lsa tx_hello tx_network_lsa tx_nssa_lsa tx_request tx_ri_lsa tx_router_lsa tx_summary_lsa tx_te_lsa", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 46")

    spirent_results_EnhancedResultsGroupFilter_28 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ospfv3_router_stats", \
    LiveFacts="adjacency_status state rx_ack rx_as_external_lsa rx_dd rx_e_as_external_lsa rx_e_inter_area_pfx_lsa rx_e_inter_area_router_lsa rx_e_intra_area_pfx_lsa rx_e_link_lsa rx_e_network_lsa rx_e_nssa_lsa rx_e_router_lsa rx_hello rx_inter_area_pfx_lsa rx_inter_area_router_lsa rx_intra_area_pfx_lsa rx_link_lsa rx_network_lsa rx_nssa_lsa rx_request rx_router_info_lsa rx_router_lsa rx_srv6_locator_lsa rx_update tx_ack tx_as_external_lsa tx_dd tx_e_as_external_lsa tx_e_inter_area_pfx_lsa tx_e_inter_area_router_lsa tx_e_intra_area_pfx_lsa tx_e_link_lsa tx_e_network_lsa tx_e_nssa_lsa tx_e_router_lsa tx_hello tx_inter_area_pfx_lsa tx_inter_area_router_lsa tx_intra_area_pfx_lsa tx_link_lsa tx_network_lsa tx_nssa_lsa tx_request tx_router_info_lsa tx_router_lsa tx_srv6_locator_lsa tx_update", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 47")

    spirent_results_EnhancedResultsConfigSelection_2 = stc.create("spirent.results.EnhancedResultsConfigSelection",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    DimensionSetName="tx_stream_config", \
    PropertyList="frames_per_second", \
    EnableAuto="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsConfigSelection 1")

    spirent_results_EnhancedResultsGroupFilter_29 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_client_assoc_stats", \
    LiveFacts="abort attempt failed failure_rate incoming_bytes incoming_traffic outgoing_bytes outgoing_traffic reading_interval success_rate successful", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 51")

    spirent_results_EnhancedResultsGroupFilter_30 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_client_stats", \
    LiveFacts="avg_rx_packet_rate avg_tx_packet_rate max_rx_packet_rate max_tx_packet_rate reading_interval rx_bandwidth rx_byte_rate rx_packet_count rx_packet_rate tx_bandwidth tx_byte_rate tx_packet_count tx_packet_rate steady_avg_tx_bandwidth steady_avg_rx_bandwidth", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 52")

    spirent_results_EnhancedResultsGroupFilter_31 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_server_stats", \
    LiveFacts="average_rx_bandwidth avg_rx_packet_rate average_tx_bandwidth avg_tx_packet_rate is_memory_limited link_map main_pool_size main_pool_used max_rx_packet_rate max_tx_packet_rate maximum_rx_bandwidth maximum_tx_bandwidth packet_memory_used reading_interval rcv_queue_length response_time rx_bandwidth rx_byte_rate rx_packet_count rx_packet_rate tx_bandwidth tx_byte_rate tx_packet_count tx_packet_rate", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 53")

    spirent_results_EnhancedResultsGroupFilter_32 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_url_client_stats", \
    LiveFacts="reading_interval average_resp_time_per_url average_resp_time_per_page maximum_resp_time_per_url url_sample_count_delta minimum_resp_time_per_url minimum_resp_time_per_page maximum_resp_time_per_page url_response_time_delta page_sample_count_delta", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 54")

    spirent_results_EnhancedResultsGroupFilter_33 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_load_spec_client_stats", \
    LiveFacts="desired_load_spec_count average_idle_time maximum_idle_time cpu_utilized minimum_idle_time current_load_spec_count steady_load_deviation_count sim_user_desired_load sim_user_current_load", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 55")

    spirent_results_EnhancedResultsGroupFilter_34 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="cptraffic_device_stats", \
    LiveFacts="state tx_pause_frame_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 56")

    spirent_results_EnhancedResultsGroupFilter_35 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_block_stats", \
    LiveFacts="state role session_count session_up_count session_idle_count session_pending_count tx_open_count rx_open_count tx_keepalive_count rx_keepalive_count tx_pc_req_count rx_pc_req_count tx_pc_rep_count rx_pc_rep_count tx_notify_count rx_notify_count tx_error_count rx_error_count tx_close_count rx_close_count flap_count tx_pc_rpt_count rx_pc_rpt_count tx_pc_upd_count rx_pc_upd_count tx_pc_init_count rx_pc_init_count total_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 57")

    spirent_results_EnhancedResultsGroupFilter_36 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_device_stats", \
    LiveFacts="state role local_ip_address peer_ip_address total_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count local_path_setup_list peer_path_setup_list local_ass_type_list peer_ass_type_list tx_open_count rx_open_count tx_keepalive_count rx_keepalive_count tx_pc_req_count rx_pc_req_count tx_pc_rep_count rx_pc_rep_count tx_pc_rpt_count rx_pc_rpt_count tx_pc_upd_count rx_pc_upd_count tx_pc_init_count rx_pc_init_count tx_notify_count tx_notify_type tx_notify_value rx_notify_count rx_notify_type rx_notify_value tx_error_count tx_error_type tx_error_value rx_error_count rx_error_type rx_error_value tx_close_count tx_close_reason rx_close_count rx_close_reason flap_count db_version", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 58")

    spirent_results_EnhancedResultsGroupFilter_37 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_lsp_block_stats", \
    LiveFacts="role lsp_count delegated_lsp_count updated_lsp_count revoked_lsp_count returned_lsp_count down_state_lsp_count up_state_lsp_count active_state_lsp_count going_down_state_lsp_count going_up_state_lsp_count other_state_lsp_count initiated_lsp_count requested_lsp_count replied_lsp_count error_lsp_count mbb_lsp_count lsp_block_local_ip_address lsp_block_peer_ip_address", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 59")

    spirent_results_EnhancedResultsGroupFilter_38 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="pcep_lsp_stats", \
    LiveFacts="role symbolic_name lsp_state plsp_state plsp_id srp_id src_ip_address dst_ip_address rp_id lsp_tx_error_type lsp_tx_error_value lsp_rx_error_type lsp_rx_error_value lsp_id tunnel_id ex_tunnel_id association_group ero lsp_local_ip_address lsp_peer_ip_address path_setup_type path_segment binding_sid", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 60")

    spirent_results_EnhancedResultsGroupFilter_39 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="cusp_block_stats", \
    LiveFacts="state session_count session_idle_count session_up_count retry_count tx_frame_count rx_frame_count tx_keepalive_count rx_keepalive_count tx_hello_count rx_hello_count rx_error_count tx_error_count rx_update_object_count tx_update_object_count tx_report_count tx_event_count rx_bras_access_ifsrvinfo_count rx_bras_user_basicinfo_count rx_bras_user_pppinfo_count rx_bras_user_ipv4info_count rx_bras_user_ipv6info_count rx_bras_user_authInfo_count rx_bras_routev4Info_count rx_bras_routev6Info_count rx_bras_static_user_ipv4_info_count rx_bras_static_user_ipv6_info_count rx_bras_user_l2tp_lac_info_count rx_bras_user_l2tp_lns_info_count rx_bras_l2tp_tunnel_lac_info_count rx_bras_l2tp_tunnel_lns_info_count tx_bras_resource_if_info_count tx_bras_resource_board_info_count tx_bras_user_traffic_Info_count tx_bras_user_detect_result_info_count tx_bras_user_nat_info_count tx_bras_user_tbl_result_count tx_cgn_addr_alloc_req_count rx_cgn_addr_alloc_ack_count tx_cgn_addr_renew_req_count rx_cgn_addr_renew_ack_count tx_cgn_addr_release_req_count rx_cgn_addr_release_ack_count tx_sync_request_count rx_sync_request_count tx_sync_begin_count rx_sync_begin_count tx_sync_data_count rx_sync_data_count tx_sync_end_count rx_sync_end_count tx_sync_ack_count rx_sync_ack_count user_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 61")

    spirent_results_EnhancedResultsGroupFilter_40 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="mld_device_stats", \
    LiveFacts="host_state tx_frame_count rx_frame_count rx_unknown_type_count rx_checksum_error_count rx_length_error_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 62")

    spirent_results_EnhancedResultsGroupFilter_41 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="mld_host_group_stats", \
    LiveFacts="duplicate_join join_fail join_latency join_timestamp leave_latency leave_timestamp state state_change_timestamp", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 63")

    spirent_results_EnhancedResultsGroupFilter_42 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_client_stats", \
    LiveFacts="bas_tx_count bas_rx_count cv_tx_count cv_rx_count cs_tx_count cs_rx_count dm_tx_count dm_rx_count dmm_tx_count dmm_rx_count dmmr_tx_count dmmr_rx_count aps_tx_count aps_rx_count rx_dropped_packet_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 64")

    spirent_results_EnhancedResultsGroupFilter_43 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_bas_stats", \
    LiveFacts="bip8_error_count rdi_status rei_count cs_lpi_status cs_lf_status cs_rf_status period_status period_error_count sequence_error_count rdi_error_count rdi_restore_count cs_lpi_error_count cs_lpi_restore_count cs_lf_error_count cs_lf_restore_count cs_rf_error_count cs_rf_restore_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 65")

    spirent_results_EnhancedResultsGroupFilter_44 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_dm_stats", \
    LiveFacts="min_delay max_delay avg_delay dm_rx_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 66")

    spirent_results_EnhancedResultsGroupFilter_45 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="flexeoam_dmmr_stats", \
    LiveFacts="min_round_trip_time max_round_trip_time avg_round_trip_time dmmr_rx_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 67")

    spirent_results_EnhancedResultsGroupFilter_46 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_fec_sym_err_stats", \
    LiveFacts="num_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 68")

    spirent_results_EnhancedResultsGroupFilter_47 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_pcs_stats", \
    LiveFacts="delay lock symbol_errors_last_sec symbol_errors_err_sec pre_fec_lane_ser rx_skew_bits symbol_error symbol_errors_per_sec sync_header_error symbol_errors_total virtual_lane_num", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 69")

    spirent_results_EnhancedResultsGroupFilter_48 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_prbs_pam4_stats", \
    LiveFacts="bitswap unsync_sec bit_errors rx_pattern sync_sec", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 70")

    spirent_results_EnhancedResultsGroupFilter_49 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_txcvrs_stats", \
    LiveFacts="lt_status los_count signal snr ctle pre_emphasis main_tap post_emphasis tx_coarse_swing", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 71")

    spirent_results_EnhancedResultsGroupFilter_50 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_lane_eyescan_stats", \
    LiveFacts="num_samples", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 72")

    spirent_results_EnhancedResultsGroupFilter_51 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l1_port_stats", \
    LiveFacts="fpga_temp module_temp module_volt link_status an_status rx_ppm_offset cw_count cw_per_bin code_violations_err_sec code_violations_total code_violations_per_sec corrected_cw_total corrected_cw_per_sec corrected_cw_last_sec code_violations_last_sec corrected_cw_err_sec symbol_errors_err_sec uncorrected_cw_last_sec all_lanes_aligned fec_lanes_aligned all_lanes_synced post_fec_ser pre_fec_ser rx_fifo_error rx_local_fault rx_remote_fault symbol_errors_per_sec symbol_errors_last_sec rx_high_ser symbol_errors_total tx_local_fault uncorrected_cw_total uncorrected_cw_per_sec uncorrected_cw_err_sec bip_error sync_header_error bip_errors_total bip_errors_last_sec bip_errors_err_sec bip_errors_per_sec control_code_errors_total control_code_errors_last_sec control_code_errors_err_sec control_code_errors_per_sec sync_header_errors_total sync_header_errors_last_sec sync_header_errors_err_sec sync_header_errors_per_sec sequence_errors_total sequence_errors_last_sec sequence_errors_err_sec sequence_errors_per_sec", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 73")

    spirent_results_EnhancedResultsGroupFilter_52 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_eot_tcp_client_stats", \
    LiveFacts="minimum_round_trip_time maximum_round_trip_time average_round_trip_time average_retransmit_time_out", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 74")

    spirent_results_EnhancedResultsGroupFilter_53 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_eot_tcp_server_stats", \
    LiveFacts="remaining_open_connections average_time_to_tcp_first_ack_of_response_data average_round_trip_time average_retransmit_time_out", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 75")

    spirent_results_EnhancedResultsGroupFilter_54 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_http_client_stats", \
    LiveFacts="reading_interval attempted_txns attempted_txns_per_sec successful_txns successful_txns_per_sec unsuccessful_txns unsuccessful_txns_per_sec aborted_txns aborted_txns_per_sec txns_awaiting_response", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 76")

    spirent_results_EnhancedResultsGroupFilter_55 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_http_server_stats", \
    LiveFacts="reading_interval open_txns completed_txns txns_per_sec average_txns_per_sec", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 77")

    spirent_results_EnhancedResultsGroupFilter_56 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_tcp_client_stats", \
    LiveFacts="reading_interval attempted_conns attempted_conn_rate cummulative_attempted_conns current_established_conns established_conn_rate cummulative_established_conns minimum_time_to_first_byte maximum_time_to_first_byte average_time_to_first_byte minimum_time_to_syn_ack maximum_time_to_syn_ack average_time_to_syn_ack minimum_estimated_server_proc_time maximum_estimated_server_proc_time average_estimated_server_proc_time conn_sample_count_delta", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 78")

    spirent_results_EnhancedResultsGroupFilter_57 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_tcp_server_stats", \
    LiveFacts="reading_interval interval_sample_count last_activity_count is_useful_data current_time_to_first_get average_to_first_get current_time_to_ack_of_first_tx_data average_to_ack_of_first_tx_data current_time_to_conn_close average_to_conn_close", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 79")

    spirent_results_EnhancedResultsGroupFilter_58 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_dl_ofdma_ru_stats", \
    LiveFacts="aid row_id ru26 ru52 ru106 ru242 ru484 ru996", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 80")

    spirent_results_EnhancedResultsGroupFilter_59 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_dl_ofdma_stats", \
    LiveFacts="ru106 ru242 ru26 ru484 ru52 ru996", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 81")

    spirent_results_EnhancedResultsGroupFilter_60 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_ul_ofdma_ru_stats", \
    LiveFacts="aid row_id ru26 ru52 ru106 ru242 ru484 ru996", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 82")

    spirent_results_EnhancedResultsGroupFilter_61 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="ieee80211_ul_ofdma_stats", \
    LiveFacts="ru106 ru242 ru26 ru484 ru52 ru996", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 83")

    spirent_results_EnhancedResultsGroupFilter_62 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="4000", \
    ResultSetName="enhl47_eot_url_client_stats", \
    LiveFacts="method attempted_txns successful_txns unsuccessful_txns aborted_txns minimum_response_time maximum_response_time average_response_time total_response_time count_of_response_time match_variable_successful match_variable_unsuccessful match_not_variable_successful match_not_variable_unsuccessful", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 84")

    spirent_results_EnhancedResultsGroupFilter_63 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l2tpv2_block_stats", \
    LiveFacts="block_state tx_pkts rx_pkts tx_acks rx_acks tx_hellos rx_hellos tx_sccreq rx_sccreq tx_sccrep rx_sccrep tx_scccon rx_scccon tx_stccnot rx_stccnot tx_wenerrornot rx_wenerrornot tx_setlinkinfo rx_setlinkinfo tx_outcallreq rx_outcallreq tx_outcallrep rx_outcallrep tx_outcallcon rx_outcallcon tx_incallreq rx_incallreq tx_incallrep rx_incallrep tx_incallcon rx_incallcon tx_calldiscnot rx_calldiscnot tunnel_setup_rate min_tunnelsetuptime max_tunnelsetuptime avg_tunnelsetuptime session_setup_rate min_sessionsetuptime max_sessionsetuptime avg_sessionsetuptime", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 85")

    spirent_results_EnhancedResultsGroupFilter_64 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l2tpv3_block_stats", \
    LiveFacts="block_state tx_pkts rx_pkts tx_acks rx_acks tx_hellos rx_hellos tx_sccreq rx_sccreq tx_sccrep rx_sccrep tx_scccon rx_scccon tx_stccnot rx_stccnot tx_wenerrornot rx_wenerrornot tx_setlinkinfo rx_setlinkinfo tx_outcallreq rx_outcallreq tx_outcallrep rx_outcallrep tx_outcallcon rx_outcallcon tx_incallreq rx_incallreq tx_incallrep rx_incallrep tx_incallcon rx_incallcon tx_calldiscnot rx_calldiscnot tunnel_setup_rate min_tunnelsetuptime max_tunnelsetuptime avg_tunnelsetuptime session_setup_rate min_sessionsetuptime max_sessionsetuptime avg_sessionsetuptime tx_csurq rx_csurq tx_csun rx_csun v3_sessionstate v3_sessionsup", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 86")

    spirent_results_EnhancedResultsGroupFilter_65 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="twamp_test_session_stats", \
    LiveFacts="state min_latency max_latency avg_latency min_jitter max_jitter avg_jitter min_server_processing_time max_server_processing_time avg_server_processing_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 87")

    spirent_results_EnhancedResultsGroupFilter_66 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="twamp_client_stats", \
    LiveFacts="client_state tx_request_session_count rx_accept_session_count rx_failed_session_count tx_start_session_count rx_start_ack_count tx_stop_session_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 88")

    spirent_results_EnhancedResultsGroupFilter_67 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="twamp_server_stats", \
    LiveFacts="server_state rx_request_session_count tx_accept_session_count tx_failed_session_count rx_start_session_count tx_start_ack_count rx_stop_session_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 89")

    spirent_results_EnhancedResultsGroupFilter_68 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="l2tp_port_stats", \
    LiveFacts="lac_count lns_count tunnels_up tunnels_down tunnels_pending_up tunnels_pending_down avg_tunnel_setup_time sessions_up sessions_down sessions_pending_up sessions_pending_down avg_session_setup_time", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 90")

    spirent_results_EnhancedResultsGroupFilter_69 = stc.create("spirent.results.EnhancedResultsGroupFilter",under = spirent_results_EnhancedResultsSelectorProfile_1, \
    RefreshInterval="1000", \
    ResultSetName="lacp_port_stats", \
    LiveFacts="state tx_lacp_pdus_count rx_lacp_pdus_count tx_marker_pdus_count rx_marker_pdus_count tx_marker_response_pdus_count rx_marker_response_pdus_count", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="spirent.results.EnhancedResultsGroupFilter 91")

# Set up relationships
    stc.config(Project_1,**{"DefaultSelection-targets" : [FrameLengthDistribution_1,CustomFillPattern_1]})
    stc.config(Tags_1,**{"DefaultTag-targets" : [Tag_1,Tag_2,Tag_3,Tag_4,Tag_5,Tag_6]})
    stc.config(PerspectiveNode_1,**{"PerspectiveChild-targets" : [ResultDataSet_1,DynamicResultView_1]})
    stc.config(PerspectiveNode_2,**{"PerspectiveChild-targets" : [ResultDataSet_1,DynamicResultView_1]})
    stc.config(Sequencer_1,**{"SequencerFinalizeType-targets" : [SequencerGroupCommand_1]})

# Set up handles
    stc.config(SequencerGroupCommand_1,CommandList="")
    stc.config(Sequencer_1,CommandList="")
    stc.config(Sequencer_1,BreakpointList="")
    stc.config(Sequencer_1,DisabledCommandList="")
    stc.config(Sequencer_1,CleanupCommand=SequencerGroupCommand_1)
    stc.config(ResultQuery_1,ResultRootList=Project_1)
    stc.config(ResultQuery_1,PropertyHandleArray="")
    stc.config(ResultQuery_2,ResultRootList=Project_1)
    stc.config(ResultQuery_2,PropertyHandleArray="")
    stc.config(PresentationResultQuery_1,FromObjects=Project_1)

    stc.config('system1',IsLoadingFromConfiguration='false')

    if len(portLocations) > 0:
        cmdResult = stc.perform('GetObjects', ClassName='Port', Condition='IsVirtual=false')
        ports = cmdResult['ObjectList'].split()
        idx = 0
        for port in ports:
            stc.config(port, location=portLocations[idx])
            idx+=1

    stc.config('project1.testResultSetting', saveResultsRelativeTo='NONE', resultsDirectory=resultsDir)
    stc.config('system1.sequencer', errorHandler='STOP_ON_ERROR')

#    connect - perform the logical to physical port mapping, connect to the 
#              chassis' and reserve the ports. This routine performs the connect,
#              reserve, and logical to physical port mappings directly.
#              The port list is retrieved from the in-memory configuration.
def connect():
    stc.perform('attachPorts')

#    apply - apply writes the logical information held in memory on the 
#            workstation to the ports in the STC chassis'.
def apply():
    stc.apply()

#    run - subscribe to any results views located in the in-memory configuration
#          and execute the sequencer and return the test status from the 
#          command sequence, if any. Test status is set by the Stopped Reason
#          in the Stop Command Sequence command. This is a string value and 
#          can be anything. If there is no sequence defined or no Stop 
#          Command Sequence command is executed, then the test state is 
#          returned. Test state can take the values: NONE, PASSED or FAILED.
def run():
    # Start the sequencer
    stc.perform('sequencerStart')

    # Wait for sequencer to finish
    testState = stc.waitUntilComplete()
    return testState

#    cleanup - release the ports, disconnect from the chassis' and reset 
#              the in-memory configuration.
def cleanup():
    stc.perform('chassisDisconnectAll')
    stc.perform('resetConfig')