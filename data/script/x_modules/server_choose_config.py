class server_choose_config():

    SPECIAL_OBJECT = [
        ".\\resources\\interface\\login\\button\\choose_server.png",
    ]

    SPECIAL_INDEX = ['301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314',
                     '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328',
                     '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342',
                     '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356',
                     '357', '358', '359', '360', '361', '362', '364', '365', '366', '367', '368', '369', '370', '371',
                     '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385',
                     '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399',
                     '404', '406', '410', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422',
                     '424', '426', '427', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439',
                     '440', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458',
                     '459', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '492',
                     '493', '494', '495', '496', '497', '498', '499', '500', '501', '502', '503', '504', '514', '515',
                     '516', '517', '518', '519', '520', '521', '522', '523', '524', '525',
                     ]

    SPECIAL_ARRAY = [
        ".\\resources\\interface\\modules\\server_choose\\server\\301.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\302.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\303.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\304.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\305.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\306.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\307.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\308.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\309.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\310.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\311.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\312.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\313.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\314.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\315.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\316.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\317.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\318.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\319.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\320.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\321.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\322.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\323.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\324.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\325.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\326.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\327.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\328.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\329.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\330.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\331.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\332.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\333.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\334.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\335.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\336.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\337.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\338.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\339.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\340.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\341.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\342.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\343.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\344.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\345.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\346.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\347.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\348.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\349.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\350.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\351.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\352.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\353.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\354.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\355.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\356.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\357.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\358.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\359.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\360.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\361.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\362.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\364.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\365.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\366.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\367.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\368.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\369.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\370.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\371.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\372.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\373.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\374.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\375.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\376.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\377.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\378.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\379.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\380.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\381.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\382.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\383.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\384.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\385.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\386.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\387.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\388.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\389.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\390.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\391.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\392.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\393.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\394.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\395.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\396.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\397.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\398.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\399.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\404.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\406.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\410.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\412.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\413.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\414.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\415.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\416.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\417.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\418.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\419.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\420.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\421.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\422.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\424.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\426.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\427.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\429.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\430.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\431.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\432.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\433.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\434.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\435.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\436.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\437.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\438.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\439.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\440.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\446.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\447.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\448.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\449.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\450.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\451.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\452.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\453.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\454.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\455.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\456.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\457.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\458.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\459.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\466.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\467.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\468.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\469.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\470.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\471.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\472.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\473.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\474.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\475.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\476.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\477.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\492.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\493.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\494.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\495.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\496.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\497.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\498.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\499.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\500.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\501.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\502.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\503.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\504.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\514.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\515.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\516.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\517.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\518.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\519.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\520.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\521.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\522.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\523.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\524.png",
        ".\\resources\\interface\\modules\\server_choose\\server\\525.png",
    ]