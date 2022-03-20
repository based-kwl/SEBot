Planet	"Gliese 667 C b"
{
	ParentBody		"Gliese 667 C"
	Class			"Terra"
	Mass 			5.94
	TidalLocked	True

	Surface
	{
		seaLevel	2
	}

	Atmosphere
	{
		Pressure		3.8
	}

	Orbit
	{
		RefPlane        "Extrasolar"
		Period          0.0197
		SemiMajorAxis   0.05041
		Eccentricity    0.13
		Inclination     22.57
		AscendingNode   39.43
		ArgOfPericenter 45.25
		MeanAnomaly     -5.42
	}
}

Planet	"Gliese 667 C c"
{
	ParentBody		"Gliese 667 C"
	Class			"Aquaria"
	Mass			3.25
	Radius          9760
	TidalLocked	True
	
	Surface
	{
		SurfStyle       0.0066806
		Randomize      (-0.526, 0.777, -0.233)
		colorDistMagn   0.072118
		colorDistFreq   1304.1
		detailScale     32768
		seaLevel        0.28244
		snowLevel       2
		tropicLatitude  0.88794
		icecapLatitude  0.7
		icecapHeight    2
		climatePole     0.4375
		climateTropic   0.40055
		climateEquator  0.64348
		climateSteppeMin -1
		climateSteppeMax -1
		climateForestMin -1
		climateForestMax -1
		climateGrassMin  -1
		climateGrassMax  -1
		humidity        1
		heightTempGrad  0.53695
		beachWidth      0.00091701
		tropicWidth     0.12333
		mainFreq        0.90487
		venusFreq       0.51319
		venusMagn       1.083
		mareFreq        0
		mareDensity     0
		terraceProb     0.38071
		erosion         0
		montesMagn      0.17052
		montesFreq      432.4
		montesSpiky     0.97451
		montesFraction  0.8885
		dunesMagn       0.05151
		dunesFreq       89.38
		dunesFraction   0.38341
		hillsMagn       0.13112
		hillsFreq       983.99
		hillsFraction   0.3682
		hills2Fraction  0.73925
		riversMagn      0
		riversFreq      3.7456
		riversSin       5.7348
		riftsMagn       0
		riftsFreq       2.7835
		riftsSin        6.2953
		canyonsMagn     0.046793
		canyonsFreq     296.88
		canyonsFraction 0.021477
		cracksMagn      0.1036
		cracksFreq      1.1059
		cracksOctaves   0
		craterMagn      0.036246
		craterFreq      72.95
		craterDensity   0
		craterOctaves   0
		volcanoMagn     0.62057
		volcanoFreq     0.63861
		volcanoDensity  0
		volcanoOctaves  0
		volcanoActivity 2
		volcanoFlows    0
		volcanoRadius   0.49352
		volcanoTemp     169.08
		lavaCoverTidal  0.21123
		lavaCoverSun    0
		lavaCoverYoung  0
		stripeZones     1
		stripeTwist     3.5
		cycloneMagn     0.61221
		cycloneDensity  0.35204
		cycloneOctaves  0
		BumpHeight      56.1
		BumpOffset      54.73
		DiffMapAlpha   "Water"
		SpecBrightWater 0.65
		SpecBrightIce   0.85
		SpecPowerWater  55
		SpecPowerIce    180
		SpecularScale   1
		RoughnessBias   0.5
		Hapke           0.7
		SpotBright      2.2895
		SpotWidth       0.05
		DayAmbient      0.07
	}

	Ocean
	{
		Depth           15.844
		Composition
		{
			H2O       	100
		}
	}

	Clouds
	{
		Height          5.6162
		Opacity         0.62
		Coverage        0.45
	}

	Atmosphere
	{
		Model          "Jupiter"
		Height          100
		Pressure        1.5
		Bright          10
		Opacity         1
		Hue             0
		Saturation      2

		Composition
		{
			N2        	72
			O2        	20
			Ar        	6
			H2O       	1.85
			CH4       	1
			CO2       	0.05
			SO2       	1e-10
		}
	}

	Orbit
	{
		RefPlane		"Extrasolar"
		Period		0.0071
		SemiMajorAxis	0.13
		Eccentricity	0.02
		Inclination	23.5
		AcendingNode	40.35
		ArgOfPericenter	292
		MeanAnomaly	292
	}
}

Planet	"Gliese 667 C f"
{
	ParentBody		"Gliese 667 C"
	Class			"Aquaria"
	Mass			2.89
	Radius		9400
	TidalLocked	True
	
	Clouds
	{
		Coverage	0.35
		Opacity	0.62
		
	}

	Ocean
	{
		Depth           54.727
		Hapke           0
		SpotBright      2
		SpotWidth       0.05
		DayAmbient      0.07
		ModulateBright  1

		Composition
		{
			H2O       	100
		}
	}	

	Atmosphere
	{
		Model		"Jupiter"
		Pressure 	1.6
		Height	150
		Bright	10
	}

	Orbit
	{
		RefPlane        "Extrasolar"
		Period          0.10684965
		SemiMajorAxis   0.156
		Eccentricity    0.03
		Inclination     23.9337714
		AscendingNode   41.0367462
		ArgOfPericenter 103
		MeanAnomaly     -103
	}
}

Planet 	"Gliese 667 C e"
{
	ParentBody		"Gliese 667 C"
	Class 		"Aquaria"
	Mass			1.888
	Radius		8000
	TidalLocked	True
	
	Surface
	{
		seaLevel 0.053435
	}

	Clouds
	{
		Coverage	0.35
		Opacity	0.62
	}
	
	Atmosphere
	{
		Model		"Jupiter"
		Pressure	12
		Height 	92
	}	

	NoRings	true

	Orbit
	{
		RefPlane		"Extrasolar"
		Period		0.1705
		SemiMajorAxis	0.156
		Eccentricity	0.02
		Inclination	24.53
		AscendingNode	40.56
		ArgOfPericenter	28.38
		MeanAnomaly	-28.38
	}

		