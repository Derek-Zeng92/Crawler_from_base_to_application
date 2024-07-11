from Crypto.Cipher import DES
import binascii

def func(a, b, c):
    if b == 0:
        return a[c:]
    d = str(a[:b])
    d += a[b + c:]
    return d


def shell(s):
    a = int(s[-1], 16) + 9
    b = int(s[a], 16)
    s = func(s, a, 1)
    a = s[b: b+8]
    data = func(s, b, 8)

    key = a.encode("utf-8")
    iv = a.encode("utf-8")

    bs = binascii.a2b_hex(data)
    aes = DES.new(key=key,mode=DES.MODE_ECB)
    result = aes.decrypt(bs)
    print(result.decode("utf-8"))


if __name__ == '__main__':
    shell("97DABE06779E5B7801522F6BFD821846F72AA8AE19A777DFBD56962581A5DF5B92683B1DF35DF99532D8443E11B52BB559F6AF331160BD15F2AA4937318F6C4DE899371E37839E5857727924E959F5C01C522C241A39F8CDAD707F8DE33FD7FF7537B057D39C388FAF2E733A6F523B9CDC52F3DCF12F74FD78A5E6DFB90F6BB8C4E8C6884568C9CDB424A618A290863B15AF216A2166A733F8980B7A6732265B5A4B79BD4ECA8A913CB6FED5B134300D9E7806DAC93243BEBE2BB8C86339C86AC0898743F94140C29F3667CA73161B1F7446BAAB95BBD4D614E49D310560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54BF221524FA9132B07EE724B3C47D3D9CCCE39E56F596B84DD1A15C6E590FD0EC6B89BF0944FD64A4DAAE487BE9E4987D31C9E8795BAC7E73362E436A3CAD794EF5F27CEE43C8A1066BB50657B3C96A8BC547D103C2FC437CCF95B2999537B6663F4C11EC9488520EBF1B48377524DC90FA3484E5D130AC9A4CD9EDA154C2CBA98A46E4D78A5F67BFB665650A6B90FF71E16A4E75D93356581453C6E2B75F7224D21B80D6680E096EE601184DA9A55056B9544C21186205BD0615AE596B8DDA582196F0A7A9FBB84218D5A90CEF327C11EC03070B19FF98C2461C2DC83F8F6F2C1B496E99C18C40DD7351370215D59CB6DD2969C04FF362869221D7E2B88CF70C92594AD15D1840708D9E15DB2684CD3511313B0D893F96E62CB137BC79E1A280157AB114530D8DD2118302189B7237CB88341E37E93D88378869DD6C62FBF2B63FDEC3A9869D93C72D07C5A7E439BB35A68FC06A3A7C0EFACCBD0B38C9BF7873B417860E01E340A8B5088999182B1B5F740C17BAEC89F91FF347118A5AB46EB3705CA9F55D13185C4DA2E11E8D2C50ACD6A719AE9A3583687346401138702DBA48EC7BE9C4C4C997A6932F7DE4564863F3A485DA8C20DD6C77E88DAE15C95F6F3328D89AAE024E254A2A3A53D4E9C2A2E73EFF16CDE569C5866E219190E1E3A8EC19481359793D511552B4A6F13668780BBABE25CF92603023BE8ADCBDE68358B9B0B733538FA6CF103E4965E88CEF734E5CA97B6E1127763BB78560F077E5D748780EDC29E3E471EB5AF549AC1501812DBFA963B49C38E2B9AE72927B5E8C8B4DCE6408AB1058D27A17BA49148A6AEB1B52BB559F6AF33108F3CB6512E1CFB818F6C4DE899371E336946C5A6AAE664E67F4DF9703612F52D1F2023202D82E4B705CA9F55D13185C55CF70E6B86EA9DCD6A719AE9A35836841676D4884A3A13007204C46BC3D2396B3814F5E9ECB58CFF3A485DA8C20DD6C42352DE19282B16A3328D89AAE024E25463FB4329890BF96E73EFF16CDE569C5866E219190E1E3A802A81482A123D96E4951893DCF104F0D0BBABE25CF92603023BE8ADCBDE68358B9B0B733538FA6CF103E4965E88CEF734E5CA97B6E1127763BB78560F077E5D73E3AF3918B1E1FF5EB5AF549AC150181FB34B5F83210B3400090915F006802BAFB9F93C83DE0E3D87A17BA49148A6AEB1B52BB559F6AF3319D2F34BF8B1733A418F6C4DE899371E34AC9746E84E2FFE854C82C2461DBC4B40F8D697FA9306BE183D1231E15D29A48696C3FB4F4AD711F983B64F27AA0E2B6960D41A2F8E82055259CB3689AFA8E66DDB60250029D5A3D568C9CDB424A618A290863B15AF216A2166A733F8980B7A60E6BC651499C8C74ECA8A913CB6FED5B15AD40F4A73DF3F92F2E2869E7ACE3FEE4B375DBDEB1D9681D778E42DB12FC9B9EE6F99BD3DF5551887F965622CF600349FF0ED47457E985CE793CD732EE63EF4BAE1FF6C5EF143D45B1991C5DCC9DD1D171AC5C7A84E9E6AD766CCD2E16B91C40E22F52182BA297BF2641E8FE6D67F47CC9C7AD4058FA71037F994C6B99FF2D137AD549A7E1266A849683DD3251019CA8BA1EE7170B5592225D0DB60553D0D92683AF166A9457FEC8EBECBC34573F08696C3FB4F4AD711FA402D71098369444661A42A550D42E03259CB3689AFA8E6646F19C5358E87E20568C9CDB424A618A6ABC7992EDCB1A16166A733F8980B7A63A6872920B6B8452ECA8A913CB6FED5B134300D9E7806DAC93243BEBE2BB8C86339C86AC0898743F94140C29F3667CA7F1ED4A28BD9B697E859BFEC93CF39E7B560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54205A970800674D1EB449DBB5CC4DF92FFF5A392621AF2221EB601ADE9B0F626EEBA1242C856A9ED6E6F5AA1DBD377A8A31C9E8795BAC7E73362E436A3CAD794EE04517FE9B38393B6BB50657B3C96A8B28ED11D4F4C459576282DEE61A92D8281A5E13053B368B2D696C3FB4F4AD711F798CB8EB83EC3630CA668081560DFDD3259CB3689AFA8E660EFBDB669BA41FEF568C9CDB424A618AF11995370DE552BC166A733F8980B7A63BFA9A1F4AC46066ECA8A913CB6FED5B134300D9E7806DAC93243BEBE2BB8C86339C86AC0898743F94140C29F3667CA73161B1F7446BAAB98D155088E6B25AF3560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54BF221524FA9132B05BC49796EB5E79F94B35D653992598914C609B7F0680A3EEDA5DF62F97C65993A0A61976401F40F131C9E8795BAC7E73362E436A3CAD794E7A2279687330AEC16BB50657B3C96A8B018C6CBBE5E4EC486ABB92BF3D3912BA5074670B018A311399128BCD400E28548F589DCEE035338A5995574F9C0E1478B08271E2D3A3AD15F07B3812C6E9F8AD06F24C382CDF0F7E37661685EAD7B590648161F4CB59261E4841445718CA1345269F1896ECAB2B06D07BE2D2B22C1BBB5BB97D5A09E4739D9E96994D1C314E28ECA029E9230FC633C1BA587E27E7BFD85A904094EC69EE9C5F81DFC4DF9397F2D88344597E4902544D67A833B001A75720615450233FAB8CD6F41C68B905BEA1FDD5F33B725729DFF385EEB4B696039B7411FD4666C948B2B76CAAD3BE121BC577C983D491D5F3562CA5D3697736865782C5366E1A78F7194F1A317A0097E2656441F72E5E09A3A1B8003000132DE58869DA5B52DC5E620F5CA3A61698B41E25A6AECA88C02BCF28696C3FB4F4AD711F667B7D2C24C7098ECA668081560DFDD3259CB3689AFA8E662C0D93A69D210DB3568C9CDB424A618AF11995370DE552BC166A733F8980B7A6B15EBD823F21072FECA8A913CB6FED5B15AD40F4A73DF3F92F2E2869E7ACE3FEE4B375DBDEB1D968FABB18B9B1B4AF329EE6F99BD3DF5551887F965622CF600349FF0ED47457E985CE793CD732EE63EF4BAE1FF6C5EF143D45B1991C5DCC9DD1D171AC5C7A84E9E6EE5DEA525812118D4743B9CD6956930F3CEEFDB1DF2C34DAD49A7F0316AD01DD86C888182E09F2D4137AD549A7E1266AFA2D71FB992863AAC23D80928F6B41D5225D0DB60553D0D9EDA79ED3742D6E9D7FE67C952C8626C8696C3FB4F4AD711F54BD6EE42BB5493D453312255BD8BBCB259CB3689AFA8E665516608C52200DD0568C9CDB424A618A29AA409A2FBE8C8A166A733F8980B7A61CA5C87EA3AE6AA44802271EA59D85D2EEA4F61BF152B6B12F2E2869E7ACE3FEE4B375DBDEB1D968CBEDC4F5319934909EE6F99BD3DF5551887F965622CF600349FF0ED47457E985CE793CD732EE63EF4BAE1FF6C5EF143D45B1991C5DCC9DD1264184AEF9BC704A8131527534C226E1D4D60CAD8801010D098E6B3D419262941B8A64F83887578A7942C0E30A806D2E137AD549A7E1266A0668E100E40F7BEF6E14093384D7D1DB225D0DB60553D0D91AAA127B331F6BAB4829DB118296B847AE81E30D9DF8EC5B705CA9F55D13185C889A9FB46FBFECA8D6A719AE9A3583681BF6A54DC964287D185BF1915632BF69DAFCA1E8142E074EF3A485DA8C20DD6C5654BA65717B33BF3328D89AAE024E25463FB4329890BF96E73EFF16CDE569C5866E219190E1E3A802A81482A123D96E1552B4A6F13668780BBABE25CF92603023BE8ADCBDE68358B9B0B733538FA6CF103E4965E88CEF734E5CA97B6E1127763BB78560F077E5D7992A0AE7093EC3B1EB5AF549AC150181C3AA1A854B6C95812A60968B68FD57693BA7D979FC167C707A17BA49148A6AEB1B52BB559F6AF331179C10E322A0B63E18F6C4DE899371E37E85150B4D92056BB24BFA905D236733497FA4C92D5EA46F33FD7FF7537B057DC2245066642668FBABBD16354379A1CA12F74FD78A5E6DFB635C8B774C20626B53549FA5DA4A7A7188D7AE23837202B2C69E1245F3F858BCE8B031E396EBA52E2FF7B6B9D095A9A461E8741880596F03FE496F345B24DF6C5A0948A3091E232A86F258DAAD273871EE6EFD901A74E0E57B3A1D9B420BAA033499F33985D255C81D31453639EAFDF60BD12D8F3B52BB948C8EEBCA514551578A1E43545E9C18E131AB6FF56901744096ACE6F92BEB83731BE7851766A2671C60EEFFE60EFA26914913C4D44A6DAB2579DCDE2777D743A411C576F6F5F82205FD0F22A844F0BB3D1D569D96316ED7D71B6243E693D66D43F5CE0A195178BFE22F30896051BA3D86696C3FB4F4AD711F983B64F27AA0E2B6960D41A2F8E82055259CB3689AFA8E66DE1D27005F91015E568C9CDB424A618A29AA409A2FBE8C8A166A733F8980B7A6F35178981E16D4034802271EA59D85D2EEA4F61BF152B6B12F2E2869E7ACE3FEE4B375DBDEB1D968EA1A81E25BE582079EE6F99BD3DF5551887F965622CF600349FF0ED47457E985CE793CD732EE63EF4BAE1FF6C5EF143D45B1991C5DCC9DD1264184AEF9BC704A7B2FBB6AE79698730084E00CC387F2277E9A75A5A5A5A2A304EDCC1350F203B7A2002731FEF32138137AD549A7E1266A849683DD3251019C274A0FCE40A0E690225D0DB60553D0D90BD2C42282FA76AF0A8E9DC0FD1135E6B2F86EAE7C91A22EA1D941103F1AA983705CA9F55D13185C889A9FB46FBFECA8D6A719AE9A358368206FF80A8CC36E48FE8EA860785D01A88DBE6D1D8A40C911F3A485DA8C20DD6C0A3685533619045D3328D89AAE024E25289838EC1D5F9D83402E5958880D55B2ECA029E9230FC633C1BA587E27E7BFD82226047C506C38945F81DFC4DF9397F2D88344597E4902544D67A833B001A75720615450233FAB8CD6F41C68B905BEA1FDD5F33B725729DF23E7F45A21B1E33A9C4F7E37333F05081A33F6DAF8B39B996FF921584ED44967529C211FA4EADD65977A18CC0D3A07514F1A317A0097E2656441F72E5E09A3A183B0C660A623059869DA5B52DC5E620FEBAEFCFD3A14AA1A7E59D22DAFD5A4544F70FF27BE8A795152BB650326EE13CB7FD05AB78FAF96475824A9272315FD49C47ECFD8E43AEAFA00FAEEC458C506F31C3DEC8BA7F11329AF04D9FF1CBED52A39BA0144A19FDBF431DBC380E3C2482F112782D7803A0D76B0B90E9E1625A0D1A6CD221A2C834D6D2196F0A7A9FBB84218D5A90CEF327C115B24870A576772EDC29A5DD24623B5D01B496E99C18C40DD7351370215D59CB6DD2969C04FF362869221D7E2B88CF70C92594AD15D1840708D9E15DB2684CD35246B67836A3319F92741D49D189B34C32CA025038C7982198EA41B749289A5DC1C4EAAF8288225698869DD6C62FBF2B61D054110A417EA64A9CB093141C950A0A68FC06A3A7C0EFA2BF97F0FCCFA27A0655E6666BD92A2E0DC10B70501F715DBB34F37D457EF44382AC6A03008965D078EB262B490532E01665A28BD367C9F9EFD5C4B4390F2AE06019398959E6A4C3CB0DFFC224ADABFF03AF893598C97AA56C2CDBD951E3EF8D2688FA9FE872F48CF563388D697A327FE94140C29F3667CA73161B1F7446BAAB95AFEB1C32A77F824560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54BF221524FA9132B07EBBF1A5F1DACD7F4B35D653992598911BA2B450FABE9886F2FAFF7C3B1000821FCEC16E85AED94B31C9E8795BAC7E73362E436A3CAD794E773BAECBE052CE636BB50657B3C96A8B25C71449109F91E60FD9A0568AB2544140F43CE4306DD671B34F37D457EF4438D3AE0A1D960BAC038EB262B490532E01665A28BD367C9F9E2F3DA39736A87C36019398959E6A4C3C68FD685B1AAD07636537B7A2704C407EC2CDBD951E3EF8D2D3950EB0761B8AAC931D2179F565BA6A79D83CC9DD3C69562196F0A7A9FBB84218D5A90CEF327C115F8BA75C71B46222B7B56A7566A24BD91B496E99C18C40DD7351370215D59CB6DD2969C04FF362869221D7E2B88CF70C92594AD15D1840708D9E15DB2684CD35E227C28400E9EB5C2741D49D189B34C35E6DF8112C841F871D73BE90062227C62AC366A5EFE5D8B68869DD6C62FBF2B6623168C7EFB267DC8C78FC7F51C4910BA68FC06A3A7C0EFA945277CB52F1D1747727DB8AB9D0D890A00FDDF6539E47758F589DCEE035338A8718B55D2D803AF2D6DF32D641323FE9B6B3F259BF641D9D7E9551566D14614237661685EAD7B5901ECB2DF6F542A1844841445718CA1345F4CECB9655200005D07BE2D2B22C1BBB5BB97D5A09E4739D9E96994D1C314E28ECA029E9230FC633C1BA587E27E7BFD8177B30FC7D9EFEE11D74F3C34CF3DF69D88344597E4902544D67A833B001A75720615450233FAB8CD6F41C68B905BEA1FDD5F33B725729DFF385EEB4B696039BCF2682B19C25EFBCB76CAAD3BE121BC507021514B418565E6F81856EF2A1BED335319660E4426E724F1A317A0097E2656441F72E5E09A3A1E3143A90927C2DC569DA5B52DC5E620FC508EED69D90D5479E4D1B15533FD8D601C2A7195CAE2D188B90B53763A445E5B34F37D457EF4438D3AE0A1D960BAC038EB262B490532E01665A28BD367C9F9E3821BD49460F8738019398959E6A4C3C68FD685B1AAD0763E50088D612085336C2CDBD951E3EF8D2688FA9FE872F48CF563388D697A327FE94140C29F3667CA7F1ED4A28BD9B697ECE4D11D495A2516D560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54205A970800674D1EB449DBB5CC4DF92FE30AD8A56E9FA64AF37FE23C82FE132A63A506ECC8A292F1B194FCE3E40D86A731C9E8795BAC7E73362E436A3CAD794ECAC00E7606EA43F76BB50657B3C96A8B311FA71191B2A56A8AF48C0FE8717A159B22A817E1746A94C671CFEFE9778E3343ED94F18B3F6836B34F37D457EF4438D3AE0A1D960BAC038EB262B490532E01C502302FCF38E6EEB6E2B000DB745455EA623F6DC7E12411CF8385BB042EB01DEA24E7F4A1C82A85C2CDBD951E3EF8D2688FA9FE872F48CF563388D697A327FE94140C29F3667CA73161B1F7446BAAB99D528F684A2180E1560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54BF221524FA9132B05BC49796EB5E79F931606D3BE14250C34BC2DBF154391F10A6A4B2E89CDA1B83B9B37A0529A03D0C31C9E8795BAC7E73362E436A3CAD794EDDEA93AC00B0D7DB6BB50657B3C96A8B68D7AFBE12F09565E8500DCAC7765C67E5EBF7EADBF3F6B2EA22394FD484E97DEA45788B3AEB4F18B34F37D457EF4438D53AD2A9A04739338EB262B490532E01793A84AE3C02CE389CC8DFBA738865D4EA623F6DC7E124114DFCA72E86C719DB6537B7A2704C407EC2CDBD951E3EF8D2688FA9FE872F48CF563388D697A327FE94140C29F3667CA73161B1F7446BAAB9062E739AE3CE1041560FCF9937C2ACAB7B47BB0FDA98AACFFB7FF55D081CEBB858CF50725388676D3C8D7ACCB469CC54205A970800674D1E7AB0F93886BBA0B4BC0ADC5DBA03142B747603FF85EA6C5E771EE99DF8340085D034D23017C7DE0031C9E8795BAC7E73362E436A3CAD794E48906FEB955450ED6BB50657B3C96A8B8ECAA108524D486AE480E25880FFDDE633FD7FF7537B057D09CC5599CD8CA0C195B28AD416213C7112F74FD78A5E6DFBFEC4A894100D893353549FA5DA4A7A71FCF7F4142D6F5678C69E1245F3F858BC6DCDE11BEBABACE5F72F2DC58EC99ADB149368C51D124B5B269BC12472F0C2C9E73EFF16CDE569C5866E219190E1E3A880F55CBF947C53FFCDD79E66A789B27E0BBABE25CF92603023BE8ADCBDE68358B9B0B733538FA6CF103E4965E88CEF734E5CA97B6E1127763BB78560F077E5D7B9C418A9DE1AFF39EB5AF549AC150181F049124E07757F0784A6B2C738817C9F0D90C58C318F3B9C7A17BA49148A6AEB1B52BB559F6AF33184F66570839DD40118F6C4DE899371E320FDE4F72006DADC987E5654C298C01AF68ECCD49D8DD7D1B26C9063EFAAAA7A33FD7FF7537B057D09CC5599CD8CA0C195B28AD416213C7112F74FD78A5E6DFB8CE04F8B6646F55E53549FA5DA4A7A71FCF7F4142D6F5678C69E1245F3F858BC6EB3EE0A0D3792C7F72F2DC58EC99ADB149368C51D124B5B269BC12472F0C2C9E73EFF16CDE569C5866E219190E1E3A8EE0EA016A40F03A27FF07B8B6748AEB40BBABE25CF92603023BE8ADCBDE68358B9B0B733538FA6CF103E4965E88CEF734E5CA97B6E1127763BB78560F077E5D795DF324F11D90A08EB5AF549AC150181BE2BBAE33847B5C3BAD6C4C9BE585F31832E9782CDB58D067A17BA49148A6AEB1B52BB559F6AF33198447AA68947413A18F6C4DE899371E3077B6921FCFDFE8729E4F5592CE15AFCA506D9DC272C3827859C0651C4BAB46483BFDFE1A8170A717F36AECC7EF66BCBAA7F7914DD7676E1DA59CCBA5C94649903AD59167D28B8D8EB46676CB86B0AA34520CDAE3D495C290AEFC3D2CE93EEA5054AA2D37D98EED7E64A77DC872543801AB968BB3BF96C1961481560731FB20864EF964A69C7BFD4D80A2C35981FC7C920891060CD070A20A3CD44E702E8B318A137C22FFC45CE61BE6530E29FED0D5637394A6B242C08A785866EFFD1CBE2898F5D8C34831826DDA1E95EF3555CFE5F158C899C2C4F061A400E4EFAC7AD0009EE23483FF3B66D321AABE96D5BB71237DC79B8B6BCB1818969C07BB9AB56FF38810519009298DB1ABF8B57145433FE80A6C93DF6F426052CAB657622F3DFF019F63C1826C38A78ACD432FC60E33981B68F589DCEE035338A8718B55D2D803AF2D6DF32D641323FE9FBDF2D1F59A72AA64F85C18C2955A4E437661685EAD7B590769F89024169A81C46D1F1D2F689EE366EDAF9876ED20238D07BE2D2B22C1BBB5BB97D5A09E4739D9E96994D1C314E28ECA029E9230FC633C1BA587E27E7BFD82226047C506C3894F31266D965273F24D88344597E4902544D67A833B001A75720615450233FAB8CD6F41C68B905BEA1FDD5F33B725729DF23E7F45A21B1E33A1EC064760AB97E062B795629086E5D127C90F19F5C74B60D0514463B8B43358D7490DC80D9DC979B876E9738A871EB59AF92F3FB273BF39633C642B3093D43348D44A70E23B68683")
