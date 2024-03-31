[step2_determine_company_clusters.txt](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/files/14817976/step2_determine_company_clusters.txt)# Defiance Capital VC Unicorn - Deep Media AI Analysis

## Overview
This project aims to analyze and visualize the clustering of companies based on various attributes such as company descriptions, underdog status, gender representation, and immigration background of leadership. By leveraging text embeddings and clustering techniques, we provide insights into the landscape of companies in our dataset.

## Features
- **Data Preprocessing**: Convert company descriptions into numerical embeddings suitable for machine learning.
- **Dimensionality Reduction**: Apply UMAP to reduce the dimensionality of embeddings for visualization.
- **Clustering Analysis**: Use KMeans to cluster companies based on their reduced embeddings.
- **Attribute Highlighting**: Highlight companies in clusters based on attributes like underdog status, female leadership, and immigration background.
- **Visualization**: Generate interactive plots to visualize clusters and their attribute distributions.

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- plotly
- umap-learn
- kaleido (for static image export with Plotly)

## Installation
Clone this repository to your local machine:
```
git clone https://github.com/RijulGupta-DM/Breadcrumbsdefiance-capital-vc-datashare.git
cd Breadcrumbsdefiance-capital-vc-datashare
```

Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage

### Data Preparation
1. Place the Defiance Capital VC analysis as a CSV file in this directory data/input/defiance_data_V1_descriptions.csv

### Running the Analysis
Execute the main script to start the analysis:
```
python main.py
```
### Results
Automatically determining the best number of clusters based on relative distances between company description text embeddings
![step1_determine_number_of_clusters](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/e1db03d4-5de6-4147-8564-201f014840c8)

Assign each company to a cluster
Cluster 0:
Flutterwave, Cambridge Mobile Telematics, Stripe, Pilot, HoneyBook, Signifyd, Zeta, Brex, Motive, ChargeBee, InDrive, 
Plaid, Navan, Melio, Assembly, Pattern, Sunbit, Public, Extend, DriveWealth, Avant, Fundbox, Ramp, Vagaro, 
Modern Treasury, Paystand, Varo Money, Pipe, Salsify, Caribou, Via, MoonPay, Tipalti, Jeeves, Vendr, 
Farmers Business Network, MX Technologies, DailyPay, Restaurant365, Chipper Cash, Papaya Global, Unit, AppDirect, 
Zebec, Gusto, Stytch, Esusu, Forter, Addepar, HighRadius, Wrapbook, Mercury, Remote, Paxos, Vise, Enable, Rippling, 
MobileCoin, Vuori, Cross River Bank, C2FO, Ripple, Upgrade, Deel, DistroKid, STORD, Cart.com, FloQast, Chime, Zip, 
OpenSea, Pave, Amount, Sift, ZenBusiness, Happy Money, Flock Safety, FLASH, Workrise, Tradeshift, Faire, OfferUp, 
Heyday, Lessen, Vice Media, Phantom, Human Interest, Current, Trumid, Acorns, Ibotta, Fetch, Stash, Placer.ai, Bolt, 
Nuro, Plume Design, M1 Holdings, Swiftly, Pax8, Printful, Betterment, Veho, Flock Freight, Guideline, FalconX, PLACE, 
Divvy Homes, Shippo, Pacaso, Thrasio, VTS, SmartAsset, Greenlight, LTK, TaxBit, CoinList, Whatnot, Upside, Fireblocks, 
CoinTracker, Flexport, Globalization Partners, Flexe, Rokt, FourKites, Flow, Project44, ShipBob, Roofstock, 
Bilt Rewards, Fabric, YipitData, Side, Loadsmart, HomeLight, Socure, Kraken, Zenoti, Avenue One, The Brandtech Group, 
Red Ventures, Weee!, Savage X Fenty, Glossier, Locus Robotics, Skims, Gemini, iTrustCapital Inc., 
TechStyle Fashion Group, AgentSync, Inxeption, GOAT Group, iCapital Network, BitGo, Carta, Capitolis, StockX, Fanatics, 
CAIS, Chainalysis, Circle, Uniswap, Clear Street, Carson Group, Anchorage Digital, Digital Currency Group, Cirkul

Cluster 1:
Coda, People.ai, 6Sense, Movable Ink, Kong, GrubMarket, Apollo.io, Sourcegraph, Workato, Highspot, Zapier, Moveworks, 
Notion, Clari, InVision, Cresta, ActiveCampaign, OutSystems, PandaDoc, ClickUp, MindTickle, Rapid, MURAL, Postman, 
Unqork, Calendly, Automation Anywhere, Mashgin, Dialpad, Paradox, Miro, Phenom, Seismic, airSlate, o9 Solutions, 
Talkdesk, Qualia, Webflow, Augury, Cameo, Lusha, Quantum Metric, Invoca, H2O.ai, Hugging Face, Apeel Sciences, Kajabi, 
Cloudinary, Iterable, Docker, Productboard, Outreach, Nextiva, Typeface, Uniphore, Snapdocs, Eightfold AI, Attentive, 
Material Bank, Copado, Gong, Netlify, Standard Cognition, Hive, ASAPP, Magic Leap, Mux, SeekOut, Masterworks, 
Magic Eden, PicsArt, Gem, Mixpanel, Retool, CaptivateIQ, SmartRecruiters, Glean, Articulate, 1047 Games, Character.AI, 
Genies, Amperity, Lattice, Envoy, Bluecore, CircleCI, Podium, SambaNova Systems, Replit, Checkr, FullStory, Intercom, 
Airbyte, VideoAmp, Handshake, CloudBees, Adept AI, Anthropic, Degreed, Pantheon, Epic Games, Imply, VerbIT, SnapLogic, 
Mythical Games, DataRobot, Pendo, Airtable, ConcertAI, AppsFlyer, PsiQuantum, BigPanda, OpenAI, Forte, DataStax, 
thatgamecompany, LaunchDarkly, Niantic, Inflection AI, Harness, Spotter, MOLOCO, Imbue, Outschool, Applied Intuition, 
ClickHouse, Density, Weights & Biases, Yotpo, Groq, Shield AI, CommerceIQ, Away, SpotOn, BloomReach, Branch, Scale AI, 
ClassDojo, OpenWeb, Automattic, Newsela, impact.com, Snorkel AI, Anyscale, Runway, Discord, Front, Domestika, Guild, 
Clubhouse, Quizlet, Skydio, MasterClass, Patreon, G2, Pony.ai, Course Hero, Cerebras Systems, Sendbird, SiFive, 
NewsBreak, Dataminr, Lucid Software, Athletic Greens, Wheel, 728, Venafi, Headspace, Aircall, Gauntlet, Alzheon, 
Dataiku

Cluster 2:
Karat, Turing.com, Andela, BitSight, At-Bay, Splashtop, Teleport, Kaseya, Aviatrix, BigID, Beyond Identity, 
Tarana Wireless, Vanta, CertiK, Netskope, ID.me, OneTrust, Persona, BlueVoyant, Vercel, Aptos, Everlaw, Alation, 
Watershed, Yuga Labs, Prove, Aura, Anduril Industries, Temporal Technologies, Astera Labs, Verkada, Opentrons, Aleo, 
CoreWeave, Astranis, Aurora Solar, Island, Relativity, Tanium, Algolia, JumpCloud, Alchemy, Axonius, 
The Boring Company, FiveTran, Incode Technologies, Tresata, Alloy, Snyk, Skydance Media, Icon, Mysten Labs, 
Axiom Space, Tealium, ReliaQuest, ABL Space Systems, Sentry, AlphaSense, Timescale, JupiterOne, Ironclad, Illumio, A24, 
ISN Software, Arcadia, dbt Labs, SpaceX, Wasabi Technologies, Boom Supersonic, Solo.io, Lookout, YugaByte, 
Unstoppable Domains, Built Technologies, Material Security, Tackle, Beta Technologies, Sisense, Immuta, Instabase, 
Orca Security, ThoughtSpot, Grafana Labs, Cribl, Crusoe Energy Systems, Lacework, ServiceTitan, Icertis, Prometheus, 
SingleStore, Chronosphere, Rubrik, Neo4j, Minio, Arctic Wolf, Vectra Networks, Sysdig, Cockroach Labs, Tekion, Reltio, 
Talos, Claroty, OwnBackup, Contrast Security, Qumulo, Electric, Noname Security, Starburst, Redis, GoodLeap, Panther, 
Salt Security, Atmosphere, Dragos, Palmetto Clean Technology, Druva, Lukka, Cohesity, VAST Data, Turntide Technologies, 
Databricks, Expel, Offchain Labs, Epirus, Exabeam, Rad Power Bikes, Boba Network, Optimism, Rebellion Defense, 
Abnormal Security, Drata, Ample, Uplight, ConsenSys, Injective, BlockDaemon, Monte Carlo, Divergent, Devo, 
Electric Hydrogen, Dremio, Helion Energy, SparkCognition, VulcanForms, Formlabs, Our Next Energy, Diamond Foundry, 
Gradiant, Solugen, Carbon, Redwood Materials, Sila Nanotechnologies, Ascend Elements, Lyten, KoBold Metals, 
Jetti Resources

Cluster 3:
Noom, Calm, Thirty Madison, SWORD Health, Somatus, Maven Clinic, Lyra Health, Modern Health, Ro, Cerebral, 
Omada Health, SonderMind, Spring Health, K Health, Elemy, Virta Health, Redesign Health, HeartFlow, Hinge Health, 
ZocDoc, Headway, Viz, Whoop, Radiology Partners, Carbon Health, Morning Consult, Kindbody, Innovaccer, Rightway, 
Devoted Health, Honor, CareBridge, Zipline, EverlyWell, Capsule, Komodo Health, DispatchHealth, Color, Nature's Fynd, 
Reify Health, Impossible Foods, BetterUp, Cityblock Health, Daily Harvest, Harry's, Medable, Chief, IntelyCare, 
Truepill, Misfits Market, Aledade, TrialSpark, Cadence Solutions, Dutchie, Sidecar Health, Collective Health, Unite Us, 
Evidation Health, UPSIDE Foods, Transcarent, Cedar, NexHealth, MasterControl, Tempus, Iodine Software, Owkin, 
Equashield, ShiftKey, Commure, Incredible Health, insitro, Clarify Health Solutions, Bowery Farming, Inari, 
Clipboard Health, Caris Life Sciences, Orca Bio, Orna Therapeutics, Visby Medical, Freenome, Zwift, Biofourmis, 
ezCater, Papa Inc., Strava, Gympass, BostonGene, Kin Insurance, The Zebra, Generate Biomedicines, Mammoth Biosciences, 
Next Insurance, Coalition, Newfront, Ethos Life, Fever, Colossal Biosciences, SeatGeek, Orchard, Tessera Therapeutics, 
Benchling, Rothy's, Gopuff, Rec Room, Glia, reddit, Grammarly, Houzz, GupShup, Pharmapacks, Thumbtack


Visualize the clusters
![step4_visualize_clusters_with_tags](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/47a215d2-720f-4923-ac78-b8d65a76673a)

Visualize "Underdog" filters

![step5_000_visualize_clusters_with_filters_female](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/89e51f46-c67b-4bcb-8ad7-a6978501b48b)
![step5_001_visualize_clusters_with_filters_gen_immigrant](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/2454150b-4de3-4d0b-a20c-78c895a5b0de)
![step5_002_visualize_clusters_with_filters_immigrant](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/d047a4e5-2ec9-4042-a2f7-d0d9511a8689)
![step5_003_visualize_clusters_with_filters_solo_founder](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/5847e250-515f-47f7-961c-21ab3c098639)
![step5_004_visualize_clusters_with_filters_serial_founder](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/24457769-9566-4725-b62d-648afbcd6c05)
![step5_005_visualize_clusters_with_filters_stem](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/1bd91f74-13dd-4991-85ef-2bc3fb977a29)
![step5_006_visualize_clusters_with_filters_female-stem](https://github.com/RijulGupta-DM/defiance-capital-vc-datashare/assets/104281028/c67dd2fb-83a5-44b6-b830-99b20ab07690)



### Customization
You can customize the analysis by modifying the `columns` variable in `main.py` to include any attributes of interest (e.g., `"female-immigrant"` for composite attributes).

## Contributing
Contributions to this project are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

## Next Steps
1. Create more advanced LLM visualizations, such as word maps overlaid on company points.
2. Label the "underdog" filtered points with company names for better interpretation of data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Remember to replace placeholders like `https://github.com/yourusername/your-repository-name.git` with your actual repository URL and adjust any specific instructions or descriptions according to what your project does. This README provides a structured outline for collaborators and users to understand and work with your project effectively.
