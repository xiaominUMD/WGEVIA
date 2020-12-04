# import pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
para = 'd'

if para == 'w':
    #data:
    wntd = [1,2,3,4,5,6]#w
    runtime = [1047.9343619346619,2528.7617015838623,5350.577814102173,8791.506373643875,12829.418137311935,16861.655007362366]
    featureGenRuntime = [0.0016727922425914686
,0.0036798762816238743
,0.005033740665406763
,0.006827170294421853
,0.008594846554707498
,0.01010690405364536
]
    wgeviaRuntime = [2894.9593341350555,6381.238715171814,12600.507453680038,20962.62832403183,30241.329400777817,40034.20350623131]
    m1a = [0.989,0.991,0.991,0.991,0.992,0.992]#model1 mlp_single
    m1std = [0.001,0.001,0.001,0.001,0.001,0.002]
    m2a = [0.99,0.992,0.991,0.993,0.993,0.993]
    m2std = [0.002,0.001,0.001,0.002,0.001,0.001]
    m3a = [0.989,0.99,0.992,0.993,0.993,0.993]
    m3std = [0.001
    ,0.001
    ,0.001
    ,0.001
    ,0.001
    ,0.001
    ]
    m4a = [0.906,0.908 ,0.911,0.913,0.913,0.914]
    m4std = [0.004,0.003,0.004,0.003,0.005,0.003
    ]

    # create figure and axis objects with subplots()
    fig,ax = plt.subplots(figsize=(16, 8))
    fs = 20
    # make a plot
    #ax.plot(, color="red", marker="o",label ='acc1')
    #ax.plot(x_axis, y_axis_3, color="red", marker="o")
    #ax.errorbar(x_axis, y_axis_3, e, marker='s', mfc='red',mec='green', ms=20, mew=4)
    ax.errorbar(wntd, m1a, m1std, uplims=True, lolims=True, label ='mlp_single acc',)
    ax.errorbar(wntd, m2a, m2std, uplims=True, lolims=True, label ='mlp_multi acc')
    ax.errorbar(wntd, m3a, m3std, uplims=True, lolims=True, label ='SVM_acc')
    ax.errorbar(wntd, m4a, m4std, uplims=True, lolims=True, label ='LDA_acc')
    ax.set_yticks(np.arange(0.9,1.01,0.01))

    # set x-axis label
    ax.set_xlabel("featureGenIters",fontsize=fs)
    # set y-axis label
    ax.set_ylabel("Test Accuracy",color="k",fontsize=fs)

    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(wntd, runtime,'m--',label ='doc2vec runtime')
    ax2.plot(wntd, wgeviaRuntime,'b--',label ='WGEVIA runtime')

    ax2.set_ylabel("Runtime (s)",color="k",fontsize=fs)

    #ax3=ax.twinx()
    #ax3.spines['right'].set_position(('outward', 120))
    # make a plot with different y-axis using second axis object
    #ax3.plot(wntd, featureGenRuntime,'b--',label ='featureExtractor runtime')
    #ax3.set_ylabel("featureExtractor runtime (s)",color="blue",fontsize=fs)

    #ax4=ax.twinx()
    #ax4.spines['right'].set_position(('outward', 240))
    # make a plot with different y-axis using second axis object
    #ax4.plot(wntd, wgeviaRuntime,'y--',label ='WGEVIA runtime')
    #ax4.set_ylabel("WGEVIA runtime (s)",color="y",fontsize=fs)


    ax.legend(loc='center left',fontsize=fs)
    ax2.legend(loc = 'center right',fontsize=fs)
    #ax3.legend(loc= (0.54,0.315),fontsize=fs)
    #ax4.legend(loc= (0.652,0.39),fontsize=fs)


    ax.tick_params(axis="x", labelsize=fs)
    ax.tick_params(axis="y", labelsize=fs)
    ax2.tick_params(axis="y", labelsize=fs)
    #ax3.tick_params(axis="y", labelsize=fs)
    #ax4.tick_params(axis="y", labelsize=fs)

    #ax.set_yticklabels(y_ticks, rotation=0, fontsize=8)

    plt.show()
    # save the plot as a file
    fig.savefig('../visOut/figure5_w_runtime_acc.png')


if para == 'nt':
    #data:
    wntd = [2,3,4,5,6,7,8,9,10,11]#d
    d = 4
    if d == 8:

        WGEVIAruntime = [6960.387296676636,7777.173343420029,8673.055312633514,11503.796628952026,13385.845479726791,15035.68401813507,16537.41446185112,18373.14762210846,20331.64,22588.4519841671]
        D2Vruntime = [6779.948984384537,7590.340972900391,8476.558032751083,8946.196504116058,8848.805790185928,8896.226517677307,8927.551693439484,8914.580554246902,8937.34,9028.258833408356]

        m2std = [0.0015067164,0.001131827,0.0012523432,0.0016192592,0.0008222568,0.0015838953,0.0016493322,0.0020855798,0.001,0.0012517127]
        m2a = [0.9817033760096428,0.9829612446070416,0.98978363828444823,0.9899677050709976,0.9900677050709976,0.9902647556070736,0.9912554880603608,0.9917200932977055,0.993,0.9929882095350819]

        m3std = [0.0014036196398073998,0.0009948391094217826,0.0017746057441196864,0.0007992909772883413,0.001175060147117923,0.0010670134611280259,0.0008953476707483259,0.001262396353541642,0.001,0.0007994706664974914]
        m3a = [0.9811752886071699,0.9826616637619822,0.9862022535352102,0.9863227579992946,0.9935950891539787,0.9925993040712862,0.9926616637619822,0.9931751462260023,0.993,0.9930782380710939]

        m1std = [0.0012870838,0.00096896384,0.00185922587,0.0012705638,0.0021112433,0.0016741959,0.00097094825,0.0014161832,0.001,0.0017345279]
        m1a = [0.9769967817508645,0.9801712160710296,0.9859382098339737,0.9856804836177424,0.9915016919991022,0.988661948524317,0.9926304839166342,0.9911587137002746,0.991,0.9912295032255856]#model1 mlp_single

        m4std = [0.004513679300941421,0.0077669201835293715,0.005144710348408305,0.003175938324297673,0.0028936770093651166,0.0028985061554579966,0.004424836314316426,0.006284121800392114,0.003,0.002673242771196047]
        m4a = [0.7519169966703457,0.7977872879702586,0.8578614049760587,0.8849859058947434,0.8884058586046319,0.9038552825858595,0.9063544253099372,0.9122107339097053,0.913,0.9138761854454928]
    else:
        # d = 4
        D2Vruntime = [6606.650731801987, 7444.659994602203,8207.686257839203,8531.089632987976,8566.16709780693,8673.365884780884,8667.756174087524,
                      8585.646532535553,8633.496286869049,8733.702984571457]
        WGEVIAruntime = [6779.662407398224,7631.9338722229,8403.142434835434,10973.707405090332,12941.707644701004,14381.99924325943,16034.469168663025,
                         17765.62677335739,20146.65927195549,21765.6560819149]

        m2std = [0.0027778393,0.0029433966,0.0025128808,0.0019286902,0.0019512653,0.002475077,0.0021525838,0.0018907154,0.0016446221,0.0018591076]
        m2a = [0.9621151972332405,0.9750560557916801,0.9769331639975631,0.9825522612248802,0.9850030992358696,0.9863337175451096,0.9873195397501591,
               0.988936809390201,0.9895018343802697,0.9900467814519727]

        m3std = [0.0033361559213859597,0.0015505877866760357,0.0016639243618771435,0.0007926158692251984,0.0007502421422134588,0.0010333236251011011,
                 0.0013943632986943857,0.0008741909319978737,0.0016177320504185502,0.0013108363160429816]
        m3a = [0.9015538839354372,0.9674473583674206,0.9810118138328194,0.9863191126066568,0.9899300647616935,0.9909882095350819,
               0.9905059069164097,0.9910817490711259,0.9919570296897341,0.992082948442258]

        m1std = [0.0032980489,0.0030634312,0.0036665339,0.0011038871,0.0031369494,0.0018011146,0.0022829322,0.0023488107,0.001480952,0.0016222977]
        m1a = [0.9227065219813155,0.9678965111723024,0.9737989088820307,0.976785552224271,0.9792906048536762,0.9803689699265976,0.9811553530699716,
               0.9826604056993768,0.9853066102359016,0.987890552357413]#model1 mlp_single

        m4std = [0.008040730319606428,0.006979300406516172,0.005771022747591194,0.0066973062447772775,0.007334192451829327,0.004229692570264949,0.009048748153334901,
                 0.004959560312789895,0.005085217356398754,0.003857238185470046]
        m4a = [0.6299493758868254,0.6644170442213082,0.7008233381210359,0.7441354718767306,0.7545773398741721,0.7736695784158845,0.7859584942593761,
               0.7884796653064374,0.8039378038846148,0.8151842857926963]


    # create figure and axis objects with subplots()
    fig,ax = plt.subplots(figsize=(16, 8))
    fs = 20
    # make a plot
    #ax.plot(, color="red", marker="o",label ='acc1')
    #ax.plot(x_axis, y_axis_3, color="red", marker="o")
    #ax.errorbar(x_axis, y_axis_3, e, marker='s', mfc='red',mec='green', ms=20, mew=4)
    ax.errorbar(wntd, m1a, m1std, uplims=True, lolims=True, label ='mlp_single acc',)
    ax.errorbar(wntd, m2a, m2std, uplims=True, lolims=True, label ='mlp_multi acc')
    ax.errorbar(wntd, m3a, m3std, uplims=True, lolims=True, label ='SVM_acc')
    ax.errorbar(wntd, m4a, m4std, uplims=True, lolims=True, label ='LDA_acc')
    ax.set_yticks(np.arange(0.6, 1.05, 0.05))
    # set x-axis label
    ax.set_xlabel("the number of channels used for graph embedding",fontsize=fs)
    # set y-axis label
    ax.set_ylabel("Test Accuracy",color="k",fontsize=fs)

    # twin object for two different y-axis on the sample plot
    #ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    #ax2.plot(wntd, D2Vruntime,'m--',label ='doc2vec runtime')
    #ax2.set_ylabel("doc2vec runtime (s)",color="m",fontsize=fs)

    ax3=ax.twinx()

    #ax3.spines['right'].set_position(('outward', 120))
    # make a plot with different y-axis using second axis object
    ax3.plot(wntd, WGEVIAruntime,'b--',label ='WGEVIA runtime')
    ax3.set_ylabel("WGEVIA runtime (s)",color="b",fontsize=fs)

    ax.legend(loc='lower right',fontsize=fs)
    #ax2.legend(loc = (0.705,0.36),fontsize=fs)
    ax3.legend(loc= (0.705,0.29),fontsize=fs)

    ax.tick_params(axis="x", labelsize=fs)
    ax.tick_params(axis="y", labelsize=fs)
    #ax2.tick_params(axis="y", labelsize=fs)
    ax3.tick_params(axis="y", labelsize=fs)
    plt.xticks(np.arange(2, 12, step=1))

    plt.show()
    # save the plot as a file
    fig.savefig('../visOut/nt_runtime_acc_d'+str(d)+'.png')


if para == 'd':
    #data:
    wntd = [2,3,4,5,6,7,8,9,10]#d
    WGEVIAruntime = [19438.4,20024.27,20164.91,20254.80,20277.65,20502.48,20884.51,21109.88,21468.18]
    D2Vruntime = [8414.18,8536.21,8563.60,8595.86,8619.26,8738.26,8843.23,8974.95,9021.11]

    m2std = [0.005, 0.0038, 0.001, 0.0016, 0.001, 0.001,0.001,0.0014,0.0009]
    m2a = [0.829,0.945,0.986,0.9868,0.9919,0.992,0.993,0.9922,0.9922]

    m3std = [0.006, 0.004, 0.0009, 0.0012,0.001, 0.001,0.001,0.001,0.0011]
    m3a = [0.689, 0.937, 0.991, 0.9916, 0.99368,0.992,0.993,0.9927,0.9929]

    m1std = [0.005, 0.0038, 0.002, 0.0017, 0.0014,0.0014,0.001,0.001,0.0008]
    m1a = [0.725,0.888,0.985,0.98728,0.989,0.9895,0.991,0.990,0.9924]#model1 mlp_single

    m4std = [0.0059, 0.007, 0.0069, 0.005, 0.0033,0.0059,0.003,0.005,0.003]
    m4a = [0.5217,0.531, 0.7948,0.845,0.8889,0.8949,0.913,0.9144,0.9256]


    # create figure and axis objects with subplots()
    fig,ax = plt.subplots(figsize=(16, 8))
    fs = 20
    # make a plot
    #ax.plot(, color="red", marker="o",label ='acc1')
    #ax.plot(x_axis, y_axis_3, color="red", marker="o")
    #ax.errorbar(x_axis, y_axis_3, e, marker='s', mfc='red',mec='green', ms=20, mew=4)
    ax.errorbar(wntd, m1a, m1std, uplims=True, lolims=True, label ='mlp_single acc',)
    ax.errorbar(wntd, m2a, m2std, uplims=True, lolims=True, label ='mlp_multi acc')
    ax.errorbar(wntd, m3a, m3std, uplims=True, lolims=True, label ='SVM_acc')
    ax.errorbar(wntd, m4a, m4std, uplims=True, lolims=True, label ='LDA_acc')
    ax.set_yticks(np.arange(0.5, 1.05, 0.05))

    # set x-axis label
    ax.set_xlabel("the dimension of the embedding vector for a single channel",fontsize=fs)
    # set y-axis label
    ax.set_ylabel("Test Accuracy",color="k",fontsize=fs)

    # twin object for two different y-axis on the sample plot
    #ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    #ax2.plot(wntd, D2Vruntime,'m--',label ='doc2vec runtime')
    #ax2.set_ylabel("doc2vec runtime (s)",color="m",fontsize=fs)

    ax3=ax.twinx()

    #ax3.spines['right'].set_position(('outward', 120))
    # make a plot with different y-axis using second axis object
    ax3.plot(wntd, WGEVIAruntime,'b--',label ='WGEVIA runtime')
    ax3.set_ylabel("WGEVIA runtime (s)",color="b",fontsize=fs)

    ax.legend(loc='lower right',fontsize=fs)
    #ax2.legend(loc = 'center right',fontsize=fs)
    ax3.legend(loc= (0.705,0.39),fontsize=fs)

    ax.tick_params(axis="x", labelsize=fs)
    ax.tick_params(axis="y", labelsize=fs)
    #ax2.tick_params(axis="y", labelsize=fs)
    ax3.tick_params(axis="y", labelsize=fs)

    plt.show()
    # save the plot as a file
    fig.savefig('../visOut/figure6_d_runtime_acc.png')
