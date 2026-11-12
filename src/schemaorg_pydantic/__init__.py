from typing import TYPE_CHECKING

from .base import Node, Ref, SchemaEnum
from .jsonld import Graph, GraphConflict, JsonLd
from .lazy import LazyExports

RELEASE = "30.1"

MODULES = {
    "AMRadioChannel": "am_radio_channel",
    "APIReference": "api_reference",
    "AboutPage": "about_page",
    "AcceptAction": "accept_action",
    "Accommodation": "accommodation",
    "AccountingService": "accounting_service",
    "AchieveAction": "achieve_action",
    "Action": "action",
    "ActionAccessSpecification": "action_access_specification",
    "ActionStatusType": "action_status_type",
    "ActivateAction": "activate_action",
    "AddAction": "add_action",
    "AdministrativeArea": "administrative_area",
    "AdultEntertainment": "adult_entertainment",
    "AdultOrientedEnumeration": "adult_oriented_enumeration",
    "AdvertiserContentArticle": "advertiser_content_article",
    "AggregateOffer": "aggregate_offer",
    "AggregateRating": "aggregate_rating",
    "AgreeAction": "agree_action",
    "Airline": "airline",
    "Airport": "airport",
    "AlignmentObject": "alignment_object",
    "AllocateAction": "allocate_action",
    "AmpStory": "amp_story",
    "AmusementPark": "amusement_park",
    "AnalysisNewsArticle": "analysis_news_article",
    "AnatomicalStructure": "anatomical_structure",
    "AnatomicalSystem": "anatomical_system",
    "AnimalShelter": "animal_shelter",
    "Answer": "answer",
    "Apartment": "apartment",
    "ApartmentComplex": "apartment_complex",
    "AppendAction": "append_action",
    "ApplyAction": "apply_action",
    "ApprovedIndication": "approved_indication",
    "Aquarium": "aquarium",
    "ArchiveComponent": "archive_component",
    "ArchiveOrganization": "archive_organization",
    "ArriveAction": "arrive_action",
    "ArtGallery": "art_gallery",
    "Artery": "artery",
    "Article": "article",
    "AskAction": "ask_action",
    "AskPublicNewsArticle": "ask_public_news_article",
    "AssessAction": "assess_action",
    "AssignAction": "assign_action",
    "Atlas": "atlas",
    "Attorney": "attorney",
    "Audience": "audience",
    "AudioObject": "audio_object",
    "AudioObjectSnapshot": "audio_object_snapshot",
    "Audiobook": "audiobook",
    "AuthenticateAction": "authenticate_action",
    "AuthorizeAction": "authorize_action",
    "AutoBodyShop": "auto_body_shop",
    "AutoDealer": "auto_dealer",
    "AutoPartsStore": "auto_parts_store",
    "AutoRental": "auto_rental",
    "AutoRepair": "auto_repair",
    "AutoWash": "auto_wash",
    "AutomatedTeller": "automated_teller",
    "AutomotiveBusiness": "automotive_business",
    "BackgroundNewsArticle": "background_news_article",
    "Bakery": "bakery",
    "BankAccount": "bank_account",
    "BankOrCreditUnion": "bank_or_credit_union",
    "BarOrPub": "bar_or_pub",
    "Barcode": "barcode",
    "Beach": "beach",
    "BeautySalon": "beauty_salon",
    "BedAndBreakfast": "bed_and_breakfast",
    "BedDetails": "bed_details",
    "BedType": "bed_type",
    "BefriendAction": "befriend_action",
    "BikeStore": "bike_store",
    "BioChemEntity": "bio_chem_entity",
    "Blog": "blog",
    "BlogPosting": "blog_posting",
    "BloodTest": "blood_test",
    "BoardingPolicyType": "boarding_policy_type",
    "BoatReservation": "boat_reservation",
    "BoatTerminal": "boat_terminal",
    "BoatTrip": "boat_trip",
    "BodyMeasurementTypeEnumeration": "body_measurement_type_enumeration",
    "BodyOfWater": "body_of_water",
    "Bone": "bone",
    "Book": "book",
    "BookFormatType": "book_format_type",
    "BookSeries": "book_series",
    "BookStore": "book_store",
    "BookmarkAction": "bookmark_action",
    "BorrowAction": "borrow_action",
    "BowlingAlley": "bowling_alley",
    "BrainStructure": "brain_structure",
    "Brand": "brand",
    "BreadcrumbList": "breadcrumb_list",
    "Brewery": "brewery",
    "Bridge": "bridge",
    "BroadcastChannel": "broadcast_channel",
    "BroadcastEvent": "broadcast_event",
    "BroadcastFrequencySpecification": "broadcast_frequency_specification",
    "BroadcastService": "broadcast_service",
    "BrokerageAccount": "brokerage_account",
    "BuddhistTemple": "buddhist_temple",
    "BusOrCoach": "bus_or_coach",
    "BusReservation": "bus_reservation",
    "BusStation": "bus_station",
    "BusStop": "bus_stop",
    "BusTrip": "bus_trip",
    "BusinessAudience": "business_audience",
    "BusinessEntityType": "business_entity_type",
    "BusinessEvent": "business_event",
    "BusinessFunction": "business_function",
    "BuyAction": "buy_action",
    "CDCPMDRecord": "cdcpmd_record",
    "CableOrSatelliteService": "cable_or_satellite_service",
    "CafeOrCoffeeShop": "cafe_or_coffee_shop",
    "Campground": "campground",
    "CampingPitch": "camping_pitch",
    "Canal": "canal",
    "CancelAction": "cancel_action",
    "Car": "car",
    "CarUsageType": "car_usage_type",
    "Casino": "casino",
    "CategoryCode": "category_code",
    "CategoryCodeSet": "category_code_set",
    "CatholicChurch": "catholic_church",
    "Cemetery": "cemetery",
    "Certification": "certification",
    "CertificationStatusEnumeration": "certification_status_enumeration",
    "Chapter": "chapter",
    "CheckAction": "check_action",
    "CheckInAction": "check_in_action",
    "CheckOutAction": "check_out_action",
    "CheckoutPage": "checkout_page",
    "ChemicalSubstance": "chemical_substance",
    "ChildCare": "child_care",
    "ChildrensEvent": "childrens_event",
    "ChooseAction": "choose_action",
    "Church": "church",
    "City": "city",
    "CityHall": "city_hall",
    "CivicStructure": "civic_structure",
    "Claim": "claim",
    "ClaimReview": "claim_review",
    "Class": "class_",
    "Clip": "clip",
    "ClothingStore": "clothing_store",
    "Collection": "collection",
    "CollectionPage": "collection_page",
    "CollegeOrUniversity": "college_or_university",
    "ComedyClub": "comedy_club",
    "ComedyEvent": "comedy_event",
    "ComicCoverArt": "comic_cover_art",
    "ComicIssue": "comic_issue",
    "ComicSeries": "comic_series",
    "ComicStory": "comic_story",
    "Comment": "comment",
    "CommentAction": "comment_action",
    "CommunicateAction": "communicate_action",
    "CompleteDataFeed": "complete_data_feed",
    "CompoundPriceSpecification": "compound_price_specification",
    "ComputerLanguage": "computer_language",
    "ComputerStore": "computer_store",
    "ConferenceEvent": "conference_event",
    "ConfirmAction": "confirm_action",
    "Consortium": "consortium",
    "ConstraintNode": "constraint_node",
    "ConsumeAction": "consume_action",
    "ContactPage": "contact_page",
    "ContactPoint": "contact_point",
    "ContactPointOption": "contact_point_option",
    "Continent": "continent",
    "ControlAction": "control_action",
    "ConvenienceStore": "convenience_store",
    "Conversation": "conversation",
    "CookAction": "cook_action",
    "Cooperative": "cooperative",
    "Corporation": "corporation",
    "CorrectionComment": "correction_comment",
    "Country": "country",
    "Course": "course",
    "CourseInstance": "course_instance",
    "Courthouse": "courthouse",
    "CoverArt": "cover_art",
    "CovidTestingFacility": "covid_testing_facility",
    "CreateAction": "create_action",
    "CreativeWork": "creative_work",
    "CreativeWorkSeason": "creative_work_season",
    "CreativeWorkSeries": "creative_work_series",
    "Credential": "credential",
    "CreditCard": "credit_card",
    "Crematorium": "crematorium",
    "CriticReview": "critic_review",
    "CurrencyConversionService": "currency_conversion_service",
    "DDxElement": "d_dx_element",
    "DENonprofitType": "de_nonprofit_type",
    "DanceEvent": "dance_event",
    "DanceGroup": "dance_group",
    "DataCatalog": "data_catalog",
    "DataDownload": "data_download",
    "DataFeed": "data_feed",
    "DataFeedItem": "data_feed_item",
    "DataType": "data_type",
    "Dataset": "dataset",
    "DayOfWeek": "day_of_week",
    "DaySpa": "day_spa",
    "DeactivateAction": "deactivate_action",
    "DeclarationOfConformity": "declaration_of_conformity",
    "DefenceEstablishment": "defence_establishment",
    "DefinedRegion": "defined_region",
    "DefinedTerm": "defined_term",
    "DefinedTermSet": "defined_term_set",
    "DeleteAction": "delete_action",
    "DeliveryChargeSpecification": "delivery_charge_specification",
    "DeliveryEvent": "delivery_event",
    "DeliveryMethod": "delivery_method",
    "Demand": "demand",
    "Dentist": "dentist",
    "DepartAction": "depart_action",
    "DepartmentStore": "department_store",
    "DepositAccount": "deposit_account",
    "DiagnosticLab": "diagnostic_lab",
    "DiagnosticProcedure": "diagnostic_procedure",
    "Diet": "diet",
    "DietarySupplement": "dietary_supplement",
    "DigitalDocument": "digital_document",
    "DigitalDocumentPermission": "digital_document_permission",
    "DigitalDocumentPermissionType": "digital_document_permission_type",
    "DigitalPlatformEnumeration": "digital_platform_enumeration",
    "DigitalProductPassport": "digital_product_passport",
    "DisagreeAction": "disagree_action",
    "DiscoverAction": "discover_action",
    "DiscussionForumPosting": "discussion_forum_posting",
    "DislikeAction": "dislike_action",
    "Distillery": "distillery",
    "DonateAction": "donate_action",
    "DoseSchedule": "dose_schedule",
    "DownloadAction": "download_action",
    "DrawAction": "draw_action",
    "Drawing": "drawing",
    "DrinkAction": "drink_action",
    "DriveWheelConfigurationValue": "drive_wheel_configuration_value",
    "Drug": "drug",
    "DrugClass": "drug_class",
    "DrugCost": "drug_cost",
    "DrugCostCategory": "drug_cost_category",
    "DrugLegalStatus": "drug_legal_status",
    "DrugPregnancyCategory": "drug_pregnancy_category",
    "DrugPrescriptionStatus": "drug_prescription_status",
    "DrugStrength": "drug_strength",
    "DryCleaningOrLaundry": "dry_cleaning_or_laundry",
    "EUEnergyEfficiencyEnumeration": "eu_energy_efficiency_enumeration",
    "EatAction": "eat_action",
    "EducationEvent": "education_event",
    "EducationalAudience": "educational_audience",
    "EducationalOccupationalCredential": "educational_occupational_credential",
    "EducationalOccupationalProgram": "educational_occupational_program",
    "EducationalOrganization": "educational_organization",
    "Electrician": "electrician",
    "ElectronicsStore": "electronics_store",
    "ElementarySchool": "elementary_school",
    "EmailMessage": "email_message",
    "Embassy": "embassy",
    "EmergencyService": "emergency_service",
    "EmployeeRole": "employee_role",
    "EmployerAggregateRating": "employer_aggregate_rating",
    "EmployerReview": "employer_review",
    "EmploymentAgency": "employment_agency",
    "EndorseAction": "endorse_action",
    "EndorsementRating": "endorsement_rating",
    "EnergyConsumptionDetails": "energy_consumption_details",
    "EnergyEfficiencyEnumeration": "energy_efficiency_enumeration",
    "EnergyStarEnergyEfficiencyEnumeration": "energy_star_energy_efficiency_enumeration",
    "EngineSpecification": "engine_specification",
    "EntertainmentBusiness": "entertainment_business",
    "EntryPoint": "entry_point",
    "Enumeration": "enumeration",
    "EnvironmentalProductDeclaration": "environmental_product_declaration",
    "Episode": "episode",
    "Error": "error",
    "Event": "event",
    "EventAttendanceModeEnumeration": "event_attendance_mode_enumeration",
    "EventReservation": "event_reservation",
    "EventSeries": "event_series",
    "EventStatusType": "event_status_type",
    "EventVenue": "event_venue",
    "ExchangeRateSpecification": "exchange_rate_specification",
    "ExerciseAction": "exercise_action",
    "ExerciseGym": "exercise_gym",
    "ExercisePlan": "exercise_plan",
    "ExhibitionEvent": "exhibition_event",
    "FAQPage": "faq_page",
    "FMRadioChannel": "fm_radio_channel",
    "FastFoodRestaurant": "fast_food_restaurant",
    "Festival": "festival",
    "FilmAction": "film_action",
    "FinancialIncentive": "financial_incentive",
    "FinancialProduct": "financial_product",
    "FinancialService": "financial_service",
    "FindAction": "find_action",
    "FireStation": "fire_station",
    "Flight": "flight",
    "FlightReservation": "flight_reservation",
    "FloorPlan": "floor_plan",
    "Florist": "florist",
    "FollowAction": "follow_action",
    "FoodEstablishment": "food_establishment",
    "FoodEstablishmentReservation": "food_establishment_reservation",
    "FoodEvent": "food_event",
    "FoodService": "food_service",
    "FulfillmentTypeEnumeration": "fulfillment_type_enumeration",
    "FundingAgency": "funding_agency",
    "FundingScheme": "funding_scheme",
    "FurnitureStore": "furniture_store",
    "Game": "game",
    "GameAvailabilityEnumeration": "game_availability_enumeration",
    "GamePlayMode": "game_play_mode",
    "GameServer": "game_server",
    "GameServerStatus": "game_server_status",
    "GardenStore": "garden_store",
    "GasStation": "gas_station",
    "GatedResidenceCommunity": "gated_residence_community",
    "GenderType": "gender_type",
    "Gene": "gene",
    "GeneralContractor": "general_contractor",
    "GeoCircle": "geo_circle",
    "GeoCoordinates": "geo_coordinates",
    "GeoShape": "geo_shape",
    "GeospatialGeometry": "geospatial_geometry",
    "GiveAction": "give_action",
    "GolfCourse": "golf_course",
    "GovernmentBenefitsType": "government_benefits_type",
    "GovernmentBuilding": "government_building",
    "GovernmentOffice": "government_office",
    "GovernmentOrganization": "government_organization",
    "GovernmentPermit": "government_permit",
    "GovernmentService": "government_service",
    "Grant": "grant",
    "GroceryStore": "grocery_store",
    "Guide": "guide",
    "HVACBusiness": "hvac_business",
    "Hackathon": "hackathon",
    "HairSalon": "hair_salon",
    "HardwareStore": "hardware_store",
    "HealthAndBeautyBusiness": "health_and_beauty_business",
    "HealthAspectEnumeration": "health_aspect_enumeration",
    "HealthClub": "health_club",
    "HealthInsurancePlan": "health_insurance_plan",
    "HealthPlanCostSharingSpecification": "health_plan_cost_sharing_specification",
    "HealthPlanFormulary": "health_plan_formulary",
    "HealthPlanNetwork": "health_plan_network",
    "HealthTopicContent": "health_topic_content",
    "HighSchool": "high_school",
    "HinduTemple": "hindu_temple",
    "HobbyShop": "hobby_shop",
    "HomeAndConstructionBusiness": "home_and_construction_business",
    "HomeGoodsStore": "home_goods_store",
    "Hospital": "hospital",
    "Hostel": "hostel",
    "Hotel": "hotel",
    "HotelRoom": "hotel_room",
    "House": "house",
    "HousePainter": "house_painter",
    "HowTo": "how_to",
    "HowToDirection": "how_to_direction",
    "HowToItem": "how_to_item",
    "HowToSection": "how_to_section",
    "HowToStep": "how_to_step",
    "HowToSupply": "how_to_supply",
    "HowToTip": "how_to_tip",
    "HowToTool": "how_to_tool",
    "HyperToc": "hyper_toc",
    "HyperTocEntry": "hyper_toc_entry",
    "IPTCDigitalSourceEnumeration": "iptc_digital_source_enumeration",
    "ITNonprofitType": "it_nonprofit_type",
    "IceCreamShop": "ice_cream_shop",
    "IgnoreAction": "ignore_action",
    "ImageGallery": "image_gallery",
    "ImageObject": "image_object",
    "ImageObjectSnapshot": "image_object_snapshot",
    "ImagingTest": "imaging_test",
    "IncentiveQualifiedExpenseType": "incentive_qualified_expense_type",
    "IncentiveStatus": "incentive_status",
    "IncentiveType": "incentive_type",
    "IndividualPhysician": "individual_physician",
    "IndividualProduct": "individual_product",
    "InfectiousAgentClass": "infectious_agent_class",
    "InfectiousDisease": "infectious_disease",
    "InformAction": "inform_action",
    "InsertAction": "insert_action",
    "InstallAction": "install_action",
    "InstantaneousEvent": "instantaneous_event",
    "InsuranceAgency": "insurance_agency",
    "Intangible": "intangible",
    "InteractAction": "interact_action",
    "InteractionCounter": "interaction_counter",
    "InternetCafe": "internet_cafe",
    "InvestmentFund": "investment_fund",
    "InvestmentOrDeposit": "investment_or_deposit",
    "InviteAction": "invite_action",
    "Invoice": "invoice",
    "ItemAvailability": "item_availability",
    "ItemList": "item_list",
    "ItemListOrderType": "item_list_order_type",
    "ItemPage": "item_page",
    "JewelryStore": "jewelry_store",
    "JobPosting": "job_posting",
    "JoinAction": "join_action",
    "Joint": "joint",
    "LakeBodyOfWater": "lake_body_of_water",
    "Landform": "landform",
    "LandmarksOrHistoricalBuildings": "landmarks_or_historical_buildings",
    "Language": "language",
    "LearningResource": "learning_resource",
    "LeaveAction": "leave_action",
    "LegalForceStatus": "legal_force_status",
    "LegalService": "legal_service",
    "LegalValueLevel": "legal_value_level",
    "Legislation": "legislation",
    "LegislationObject": "legislation_object",
    "LegislativeBuilding": "legislative_building",
    "LendAction": "lend_action",
    "Library": "library",
    "LibrarySystem": "library_system",
    "LifestyleModification": "lifestyle_modification",
    "Ligament": "ligament",
    "LikeAction": "like_action",
    "LinkRole": "link_role",
    "LiquorStore": "liquor_store",
    "ListItem": "list_item",
    "ListenAction": "listen_action",
    "LiteraryEvent": "literary_event",
    "LiveBlogPosting": "live_blog_posting",
    "LoanOrCredit": "loan_or_credit",
    "LocalBusiness": "local_business",
    "LocationFeatureSpecification": "location_feature_specification",
    "Locksmith": "locksmith",
    "LodgingBusiness": "lodging_business",
    "LodgingReservation": "lodging_reservation",
    "LoginAction": "login_action",
    "LoseAction": "lose_action",
    "LymphaticVessel": "lymphatic_vessel",
    "Manuscript": "manuscript",
    "Map": "map",
    "MapCategoryType": "map_category_type",
    "MarryAction": "marry_action",
    "MathSolver": "math_solver",
    "MaximumDoseSchedule": "maximum_dose_schedule",
    "MeasurementMethodEnum": "measurement_method_enum",
    "MeasurementTypeEnumeration": "measurement_type_enumeration",
    "MediaEnumeration": "media_enumeration",
    "MediaGallery": "media_gallery",
    "MediaManipulationRatingEnumeration": "media_manipulation_rating_enumeration",
    "MediaObject": "media_object",
    "MediaReview": "media_review",
    "MediaReviewItem": "media_review_item",
    "MediaSubscription": "media_subscription",
    "MedicalAudience": "medical_audience",
    "MedicalAudienceType": "medical_audience_type",
    "MedicalBusiness": "medical_business",
    "MedicalCause": "medical_cause",
    "MedicalClinic": "medical_clinic",
    "MedicalCode": "medical_code",
    "MedicalCondition": "medical_condition",
    "MedicalConditionStage": "medical_condition_stage",
    "MedicalContraindication": "medical_contraindication",
    "MedicalDevice": "medical_device",
    "MedicalDevicePurpose": "medical_device_purpose",
    "MedicalEntity": "medical_entity",
    "MedicalEnumeration": "medical_enumeration",
    "MedicalEvidenceLevel": "medical_evidence_level",
    "MedicalGuideline": "medical_guideline",
    "MedicalGuidelineContraindication": "medical_guideline_contraindication",
    "MedicalGuidelineRecommendation": "medical_guideline_recommendation",
    "MedicalImagingTechnique": "medical_imaging_technique",
    "MedicalIndication": "medical_indication",
    "MedicalIntangible": "medical_intangible",
    "MedicalObservationalStudy": "medical_observational_study",
    "MedicalObservationalStudyDesign": "medical_observational_study_design",
    "MedicalOrganization": "medical_organization",
    "MedicalProcedure": "medical_procedure",
    "MedicalProcedureType": "medical_procedure_type",
    "MedicalRiskCalculator": "medical_risk_calculator",
    "MedicalRiskEstimator": "medical_risk_estimator",
    "MedicalRiskFactor": "medical_risk_factor",
    "MedicalRiskScore": "medical_risk_score",
    "MedicalScholarlyArticle": "medical_scholarly_article",
    "MedicalSign": "medical_sign",
    "MedicalSignOrSymptom": "medical_sign_or_symptom",
    "MedicalSpecialty": "medical_specialty",
    "MedicalStudy": "medical_study",
    "MedicalStudyStatus": "medical_study_status",
    "MedicalSymptom": "medical_symptom",
    "MedicalTest": "medical_test",
    "MedicalTestPanel": "medical_test_panel",
    "MedicalTherapy": "medical_therapy",
    "MedicalTrial": "medical_trial",
    "MedicalTrialDesign": "medical_trial_design",
    "MedicalWebPage": "medical_web_page",
    "MedicineSystem": "medicine_system",
    "MeetingRoom": "meeting_room",
    "MemberProgram": "member_program",
    "MemberProgramTier": "member_program_tier",
    "MensClothingStore": "mens_clothing_store",
    "Menu": "menu",
    "MenuItem": "menu_item",
    "MenuSection": "menu_section",
    "MerchantReturnEnumeration": "merchant_return_enumeration",
    "MerchantReturnPolicy": "merchant_return_policy",
    "MerchantReturnPolicySeasonalOverride": "merchant_return_policy_seasonal_override",
    "Message": "message",
    "MiddleSchool": "middle_school",
    "MobileApplication": "mobile_application",
    "MobilePhoneStore": "mobile_phone_store",
    "MolecularEntity": "molecular_entity",
    "MonetaryAmount": "monetary_amount",
    "MonetaryAmountDistribution": "monetary_amount_distribution",
    "MonetaryGrant": "monetary_grant",
    "MoneyTransfer": "money_transfer",
    "MortgageLoan": "mortgage_loan",
    "Mosque": "mosque",
    "Motel": "motel",
    "Motorcycle": "motorcycle",
    "MotorcycleDealer": "motorcycle_dealer",
    "MotorcycleRepair": "motorcycle_repair",
    "MotorizedBicycle": "motorized_bicycle",
    "Mountain": "mountain",
    "MoveAction": "move_action",
    "Movie": "movie",
    "MovieClip": "movie_clip",
    "MovieRentalStore": "movie_rental_store",
    "MovieSeries": "movie_series",
    "MovieTheater": "movie_theater",
    "MovingCompany": "moving_company",
    "Muscle": "muscle",
    "Museum": "museum",
    "MusicAlbum": "music_album",
    "MusicAlbumProductionType": "music_album_production_type",
    "MusicAlbumReleaseType": "music_album_release_type",
    "MusicComposition": "music_composition",
    "MusicEvent": "music_event",
    "MusicGroup": "music_group",
    "MusicPlaylist": "music_playlist",
    "MusicRecording": "music_recording",
    "MusicRelease": "music_release",
    "MusicReleaseFormatType": "music_release_format_type",
    "MusicStore": "music_store",
    "MusicVenue": "music_venue",
    "MusicVideoObject": "music_video_object",
    "NGO": "ngo",
    "NLNonprofitType": "nl_nonprofit_type",
    "NailSalon": "nail_salon",
    "Nerve": "nerve",
    "NewsArticle": "news_article",
    "NewsMediaOrganization": "news_media_organization",
    "Newspaper": "newspaper",
    "NightClub": "night_club",
    "NonprofitType": "nonprofit_type",
    "Notary": "notary",
    "NoteDigitalDocument": "note_digital_document",
    "NutritionInformation": "nutrition_information",
    "Observation": "observation",
    "Occupation": "occupation",
    "OccupationalExperienceRequirements": "occupational_experience_requirements",
    "OccupationalTherapy": "occupational_therapy",
    "OceanBodyOfWater": "ocean_body_of_water",
    "Offer": "offer",
    "OfferCatalog": "offer_catalog",
    "OfferForLease": "offer_for_lease",
    "OfferForPurchase": "offer_for_purchase",
    "OfferItemCondition": "offer_item_condition",
    "OfferShippingDetails": "offer_shipping_details",
    "OfficeEquipmentStore": "office_equipment_store",
    "OnDemandEvent": "on_demand_event",
    "OnlineBusiness": "online_business",
    "OnlineMarketplace": "online_marketplace",
    "OnlineStore": "online_store",
    "OpeningHoursSpecification": "opening_hours_specification",
    "OperatingSystem": "operating_system",
    "OpinionNewsArticle": "opinion_news_article",
    "Optician": "optician",
    "Order": "order",
    "OrderAction": "order_action",
    "OrderItem": "order_item",
    "OrderStatus": "order_status",
    "Organization": "organization",
    "OrganizationRole": "organization_role",
    "OrganizeAction": "organize_action",
    "OutletStore": "outlet_store",
    "OwnershipInfo": "ownership_info",
    "PaintAction": "paint_action",
    "Painting": "painting",
    "PalliativeProcedure": "palliative_procedure",
    "ParcelDelivery": "parcel_delivery",
    "ParentAudience": "parent_audience",
    "Park": "park",
    "ParkingFacility": "parking_facility",
    "PathologyTest": "pathology_test",
    "Patient": "patient",
    "PawnShop": "pawn_shop",
    "PayAction": "pay_action",
    "PaymentCard": "payment_card",
    "PaymentChargeSpecification": "payment_charge_specification",
    "PaymentMethod": "payment_method",
    "PaymentMethodType": "payment_method_type",
    "PaymentService": "payment_service",
    "PaymentStatusType": "payment_status_type",
    "PeopleAudience": "people_audience",
    "PerformAction": "perform_action",
    "PerformanceRole": "performance_role",
    "PerformingArtsEvent": "performing_arts_event",
    "PerformingArtsTheater": "performing_arts_theater",
    "PerformingGroup": "performing_group",
    "Periodical": "periodical",
    "Permit": "permit",
    "Person": "person",
    "PetStore": "pet_store",
    "Pharmacy": "pharmacy",
    "Photograph": "photograph",
    "PhotographAction": "photograph_action",
    "PhysicalActivity": "physical_activity",
    "PhysicalActivityCategory": "physical_activity_category",
    "PhysicalExam": "physical_exam",
    "PhysicalTherapy": "physical_therapy",
    "Physician": "physician",
    "PhysiciansOffice": "physicians_office",
    "Place": "place",
    "PlaceOfWorship": "place_of_worship",
    "PlanAction": "plan_action",
    "Play": "play",
    "PlayAction": "play_action",
    "PlayGameAction": "play_game_action",
    "Playground": "playground",
    "Plumber": "plumber",
    "PodcastEpisode": "podcast_episode",
    "PodcastSeason": "podcast_season",
    "PodcastSeries": "podcast_series",
    "PoliceStation": "police_station",
    "PoliticalParty": "political_party",
    "Pond": "pond",
    "PostOffice": "post_office",
    "PostalAddress": "postal_address",
    "PostalCodeRangeSpecification": "postal_code_range_specification",
    "Poster": "poster",
    "PreOrderAction": "pre_order_action",
    "PrependAction": "prepend_action",
    "Preschool": "preschool",
    "PresentationDigitalDocument": "presentation_digital_document",
    "PreventionIndication": "prevention_indication",
    "PriceComponentTypeEnumeration": "price_component_type_enumeration",
    "PriceSpecification": "price_specification",
    "PriceTypeEnumeration": "price_type_enumeration",
    "Product": "product",
    "ProductCollection": "product_collection",
    "ProductGroup": "product_group",
    "ProductModel": "product_model",
    "ProfessionalService": "professional_service",
    "ProfilePage": "profile_page",
    "ProgramMembership": "program_membership",
    "Project": "project",
    "Property": "property",
    "PropertyValue": "property_value",
    "PropertyValueSpecification": "property_value_specification",
    "Protein": "protein",
    "PsychologicalTreatment": "psychological_treatment",
    "PublicSwimmingPool": "public_swimming_pool",
    "PublicToilet": "public_toilet",
    "PublicationEvent": "publication_event",
    "PublicationIssue": "publication_issue",
    "PublicationVolume": "publication_volume",
    "PurchaseType": "purchase_type",
    "QAPage": "qa_page",
    "QualitativeValue": "qualitative_value",
    "QuantitativeValue": "quantitative_value",
    "QuantitativeValueDistribution": "quantitative_value_distribution",
    "Question": "question",
    "Quiz": "quiz",
    "Quotation": "quotation",
    "QuoteAction": "quote_action",
    "RVPark": "rv_park",
    "RadiationTherapy": "radiation_therapy",
    "RadioBroadcastService": "radio_broadcast_service",
    "RadioChannel": "radio_channel",
    "RadioClip": "radio_clip",
    "RadioEpisode": "radio_episode",
    "RadioSeason": "radio_season",
    "RadioSeries": "radio_series",
    "RadioStation": "radio_station",
    "Rating": "rating",
    "ReactAction": "react_action",
    "ReadAction": "read_action",
    "RealEstateAgent": "real_estate_agent",
    "RealEstateListing": "real_estate_listing",
    "ReceiveAction": "receive_action",
    "Recipe": "recipe",
    "Recommendation": "recommendation",
    "RecommendedDoseSchedule": "recommended_dose_schedule",
    "RecyclingCenter": "recycling_center",
    "RefundTypeEnumeration": "refund_type_enumeration",
    "RegisterAction": "register_action",
    "RejectAction": "reject_action",
    "RentAction": "rent_action",
    "RentalCarReservation": "rental_car_reservation",
    "RepaymentSpecification": "repayment_specification",
    "ReplaceAction": "replace_action",
    "ReplyAction": "reply_action",
    "Report": "report",
    "ReportageNewsArticle": "reportage_news_article",
    "ReportedDoseSchedule": "reported_dose_schedule",
    "ResearchOrganization": "research_organization",
    "ResearchProject": "research_project",
    "Researcher": "researcher",
    "Reservation": "reservation",
    "ReservationPackage": "reservation_package",
    "ReservationStatusType": "reservation_status_type",
    "ReserveAction": "reserve_action",
    "Reservoir": "reservoir",
    "ResetPasswordAction": "reset_password_action",
    "Residence": "residence",
    "Resort": "resort",
    "Restaurant": "restaurant",
    "RestrictedDiet": "restricted_diet",
    "ResumeAction": "resume_action",
    "ReturnAction": "return_action",
    "ReturnFeesEnumeration": "return_fees_enumeration",
    "ReturnLabelSourceEnumeration": "return_label_source_enumeration",
    "ReturnMethodEnumeration": "return_method_enumeration",
    "Review": "review",
    "ReviewAction": "review_action",
    "ReviewNewsArticle": "review_news_article",
    "RiverBodyOfWater": "river_body_of_water",
    "Role": "role",
    "RoofingContractor": "roofing_contractor",
    "Room": "room",
    "RsvpAction": "rsvp_action",
    "RsvpResponseType": "rsvp_response_type",
    "RuntimePlatform": "runtime_platform",
    "SaleEvent": "sale_event",
    "SatiricalArticle": "satirical_article",
    "Schedule": "schedule",
    "ScheduleAction": "schedule_action",
    "ScholarlyArticle": "scholarly_article",
    "School": "school",
    "SchoolDistrict": "school_district",
    "ScreeningEvent": "screening_event",
    "Sculpture": "sculpture",
    "SeaBodyOfWater": "sea_body_of_water",
    "SearchAction": "search_action",
    "SearchRescueOrganization": "search_rescue_organization",
    "SearchResultsPage": "search_results_page",
    "Seat": "seat",
    "SeekToAction": "seek_to_action",
    "SelfStorage": "self_storage",
    "SellAction": "sell_action",
    "SendAction": "send_action",
    "SequentialArt": "sequential_art",
    "Series": "series",
    "Service": "service",
    "ServiceChannel": "service_channel",
    "ServicePeriod": "service_period",
    "ShareAction": "share_action",
    "SheetMusic": "sheet_music",
    "ShippingConditions": "shipping_conditions",
    "ShippingDeliveryTime": "shipping_delivery_time",
    "ShippingRateSettings": "shipping_rate_settings",
    "ShippingService": "shipping_service",
    "ShoeStore": "shoe_store",
    "ShoppingCenter": "shopping_center",
    "ShortStory": "short_story",
    "SingleFamilyResidence": "single_family_residence",
    "SiteNavigationElement": "site_navigation_element",
    "SizeGroupEnumeration": "size_group_enumeration",
    "SizeSpecification": "size_specification",
    "SizeSystemEnumeration": "size_system_enumeration",
    "SkiResort": "ski_resort",
    "SocialEvent": "social_event",
    "SocialMediaPosting": "social_media_posting",
    "SoftwareApplication": "software_application",
    "SoftwareSourceCode": "software_source_code",
    "SolveMathAction": "solve_math_action",
    "SomeProducts": "some_products",
    "SpeakableSpecification": "speakable_specification",
    "SpecialAnnouncement": "special_announcement",
    "Specialty": "specialty",
    "SportingGoodsStore": "sporting_goods_store",
    "SportsActivityLocation": "sports_activity_location",
    "SportsClub": "sports_club",
    "SportsEvent": "sports_event",
    "SportsOrganization": "sports_organization",
    "SportsTeam": "sports_team",
    "SpreadsheetDigitalDocument": "spreadsheet_digital_document",
    "StadiumOrArena": "stadium_or_arena",
    "State": "state",
    "Statement": "statement",
    "StatisticalPopulation": "statistical_population",
    "StatisticalVariable": "statistical_variable",
    "StatusEnumeration": "status_enumeration",
    "SteeringPositionValue": "steering_position_value",
    "Store": "store",
    "StructuredValue": "structured_value",
    "SubscribeAction": "subscribe_action",
    "Substance": "substance",
    "SubwayStation": "subway_station",
    "Suite": "suite",
    "SuperficialAnatomy": "superficial_anatomy",
    "SurgicalProcedure": "surgical_procedure",
    "SuspendAction": "suspend_action",
    "Syllabus": "syllabus",
    "Synagogue": "synagogue",
    "TVClip": "tv_clip",
    "TVEpisode": "tv_episode",
    "TVSeason": "tv_season",
    "TVSeries": "tv_series",
    "Table": "table",
    "TakeAction": "take_action",
    "TattooParlor": "tattoo_parlor",
    "TaxiReservation": "taxi_reservation",
    "TaxiService": "taxi_service",
    "TaxiStand": "taxi_stand",
    "Taxon": "taxon",
    "TechArticle": "tech_article",
    "TelevisionChannel": "television_channel",
    "TelevisionStation": "television_station",
    "TennisComplex": "tennis_complex",
    "TextDigitalDocument": "text_digital_document",
    "TextObject": "text_object",
    "TheaterEvent": "theater_event",
    "TheaterGroup": "theater_group",
    "TherapeuticProcedure": "therapeutic_procedure",
    "Thesis": "thesis",
    "Thing": "thing",
    "ThreeDModel": "three_d_model",
    "Ticket": "ticket",
    "TieAction": "tie_action",
    "TierBenefitEnumeration": "tier_benefit_enumeration",
    "TipAction": "tip_action",
    "TireShop": "tire_shop",
    "TouristAttraction": "tourist_attraction",
    "TouristDestination": "tourist_destination",
    "TouristInformationCenter": "tourist_information_center",
    "TouristTrip": "tourist_trip",
    "ToyStore": "toy_store",
    "TrackAction": "track_action",
    "TradeAction": "trade_action",
    "TrainReservation": "train_reservation",
    "TrainStation": "train_station",
    "TrainTrip": "train_trip",
    "TransferAction": "transfer_action",
    "TravelAction": "travel_action",
    "TravelAgency": "travel_agency",
    "TreatmentIndication": "treatment_indication",
    "Trip": "trip",
    "TypeAndQuantityNode": "type_and_quantity_node",
    "UKNonprofitType": "uk_nonprofit_type",
    "USNonprofitType": "us_nonprofit_type",
    "UnRegisterAction": "un_register_action",
    "UnitPriceSpecification": "unit_price_specification",
    "UpdateAction": "update_action",
    "UseAction": "use_action",
    "UserReview": "user_review",
    "VacationRental": "vacation_rental",
    "Vehicle": "vehicle",
    "Vein": "vein",
    "Vessel": "vessel",
    "VeterinaryCare": "veterinary_care",
    "VideoGallery": "video_gallery",
    "VideoGame": "video_game",
    "VideoGameClip": "video_game_clip",
    "VideoGameSeries": "video_game_series",
    "VideoObject": "video_object",
    "VideoObjectSnapshot": "video_object_snapshot",
    "ViewAction": "view_action",
    "VirtualLocation": "virtual_location",
    "VisualArtsEvent": "visual_arts_event",
    "VisualArtwork": "visual_artwork",
    "VitalSign": "vital_sign",
    "Volcano": "volcano",
    "VoteAction": "vote_action",
    "WPAdBlock": "wp_ad_block",
    "WPFooter": "wp_footer",
    "WPHeader": "wp_header",
    "WPSideBar": "wp_side_bar",
    "WantAction": "want_action",
    "WarrantyPromise": "warranty_promise",
    "WarrantyScope": "warranty_scope",
    "WatchAction": "watch_action",
    "Waterfall": "waterfall",
    "WearAction": "wear_action",
    "WearableMeasurementTypeEnumeration": "wearable_measurement_type_enumeration",
    "WearableSizeGroupEnumeration": "wearable_size_group_enumeration",
    "WearableSizeSystemEnumeration": "wearable_size_system_enumeration",
    "WebAPI": "web_api",
    "WebApplication": "web_application",
    "WebContent": "web_content",
    "WebPage": "web_page",
    "WebPageElement": "web_page_element",
    "WebSite": "web_site",
    "WholesaleStore": "wholesale_store",
    "WinAction": "win_action",
    "Winery": "winery",
    "WorkBasedProgram": "work_based_program",
    "WorkersUnion": "workers_union",
    "WriteAction": "write_action",
    "Zoo": "zoo",
}

lazy = LazyExports(__name__, MODULES)
__getattr__ = lazy.get
__dir__ = lazy.names

if TYPE_CHECKING:
    from .models.am_radio_channel import AMRadioChannel
    from .models.api_reference import APIReference
    from .models.about_page import AboutPage
    from .models.accept_action import AcceptAction
    from .models.accommodation import Accommodation
    from .models.accounting_service import AccountingService
    from .models.achieve_action import AchieveAction
    from .models.action import Action
    from .models.action_access_specification import ActionAccessSpecification
    from .models.action_status_type import ActionStatusType
    from .models.activate_action import ActivateAction
    from .models.add_action import AddAction
    from .models.administrative_area import AdministrativeArea
    from .models.adult_entertainment import AdultEntertainment
    from .models.adult_oriented_enumeration import AdultOrientedEnumeration
    from .models.advertiser_content_article import AdvertiserContentArticle
    from .models.aggregate_offer import AggregateOffer
    from .models.aggregate_rating import AggregateRating
    from .models.agree_action import AgreeAction
    from .models.airline import Airline
    from .models.airport import Airport
    from .models.alignment_object import AlignmentObject
    from .models.allocate_action import AllocateAction
    from .models.amp_story import AmpStory
    from .models.amusement_park import AmusementPark
    from .models.analysis_news_article import AnalysisNewsArticle
    from .models.anatomical_structure import AnatomicalStructure
    from .models.anatomical_system import AnatomicalSystem
    from .models.animal_shelter import AnimalShelter
    from .models.answer import Answer
    from .models.apartment import Apartment
    from .models.apartment_complex import ApartmentComplex
    from .models.append_action import AppendAction
    from .models.apply_action import ApplyAction
    from .models.approved_indication import ApprovedIndication
    from .models.aquarium import Aquarium
    from .models.archive_component import ArchiveComponent
    from .models.archive_organization import ArchiveOrganization
    from .models.arrive_action import ArriveAction
    from .models.art_gallery import ArtGallery
    from .models.artery import Artery
    from .models.article import Article
    from .models.ask_action import AskAction
    from .models.ask_public_news_article import AskPublicNewsArticle
    from .models.assess_action import AssessAction
    from .models.assign_action import AssignAction
    from .models.atlas import Atlas
    from .models.attorney import Attorney
    from .models.audience import Audience
    from .models.audio_object import AudioObject
    from .models.audio_object_snapshot import AudioObjectSnapshot
    from .models.audiobook import Audiobook
    from .models.authenticate_action import AuthenticateAction
    from .models.authorize_action import AuthorizeAction
    from .models.auto_body_shop import AutoBodyShop
    from .models.auto_dealer import AutoDealer
    from .models.auto_parts_store import AutoPartsStore
    from .models.auto_rental import AutoRental
    from .models.auto_repair import AutoRepair
    from .models.auto_wash import AutoWash
    from .models.automated_teller import AutomatedTeller
    from .models.automotive_business import AutomotiveBusiness
    from .models.background_news_article import BackgroundNewsArticle
    from .models.bakery import Bakery
    from .models.bank_account import BankAccount
    from .models.bank_or_credit_union import BankOrCreditUnion
    from .models.bar_or_pub import BarOrPub
    from .models.barcode import Barcode
    from .models.beach import Beach
    from .models.beauty_salon import BeautySalon
    from .models.bed_and_breakfast import BedAndBreakfast
    from .models.bed_details import BedDetails
    from .models.bed_type import BedType
    from .models.befriend_action import BefriendAction
    from .models.bike_store import BikeStore
    from .models.bio_chem_entity import BioChemEntity
    from .models.blog import Blog
    from .models.blog_posting import BlogPosting
    from .models.blood_test import BloodTest
    from .models.boarding_policy_type import BoardingPolicyType
    from .models.boat_reservation import BoatReservation
    from .models.boat_terminal import BoatTerminal
    from .models.boat_trip import BoatTrip
    from .models.body_measurement_type_enumeration import BodyMeasurementTypeEnumeration
    from .models.body_of_water import BodyOfWater
    from .models.bone import Bone
    from .models.book import Book
    from .models.book_format_type import BookFormatType
    from .models.book_series import BookSeries
    from .models.book_store import BookStore
    from .models.bookmark_action import BookmarkAction
    from .models.borrow_action import BorrowAction
    from .models.bowling_alley import BowlingAlley
    from .models.brain_structure import BrainStructure
    from .models.brand import Brand
    from .models.breadcrumb_list import BreadcrumbList
    from .models.brewery import Brewery
    from .models.bridge import Bridge
    from .models.broadcast_channel import BroadcastChannel
    from .models.broadcast_event import BroadcastEvent
    from .models.broadcast_frequency_specification import BroadcastFrequencySpecification
    from .models.broadcast_service import BroadcastService
    from .models.brokerage_account import BrokerageAccount
    from .models.buddhist_temple import BuddhistTemple
    from .models.bus_or_coach import BusOrCoach
    from .models.bus_reservation import BusReservation
    from .models.bus_station import BusStation
    from .models.bus_stop import BusStop
    from .models.bus_trip import BusTrip
    from .models.business_audience import BusinessAudience
    from .models.business_entity_type import BusinessEntityType
    from .models.business_event import BusinessEvent
    from .models.business_function import BusinessFunction
    from .models.buy_action import BuyAction
    from .models.cdcpmd_record import CDCPMDRecord
    from .models.cable_or_satellite_service import CableOrSatelliteService
    from .models.cafe_or_coffee_shop import CafeOrCoffeeShop
    from .models.campground import Campground
    from .models.camping_pitch import CampingPitch
    from .models.canal import Canal
    from .models.cancel_action import CancelAction
    from .models.car import Car
    from .models.car_usage_type import CarUsageType
    from .models.casino import Casino
    from .models.category_code import CategoryCode
    from .models.category_code_set import CategoryCodeSet
    from .models.catholic_church import CatholicChurch
    from .models.cemetery import Cemetery
    from .models.certification import Certification
    from .models.certification_status_enumeration import CertificationStatusEnumeration
    from .models.chapter import Chapter
    from .models.check_action import CheckAction
    from .models.check_in_action import CheckInAction
    from .models.check_out_action import CheckOutAction
    from .models.checkout_page import CheckoutPage
    from .models.chemical_substance import ChemicalSubstance
    from .models.child_care import ChildCare
    from .models.childrens_event import ChildrensEvent
    from .models.choose_action import ChooseAction
    from .models.church import Church
    from .models.city import City
    from .models.city_hall import CityHall
    from .models.civic_structure import CivicStructure
    from .models.claim import Claim
    from .models.claim_review import ClaimReview
    from .models.class_ import Class
    from .models.clip import Clip
    from .models.clothing_store import ClothingStore
    from .models.collection import Collection
    from .models.collection_page import CollectionPage
    from .models.college_or_university import CollegeOrUniversity
    from .models.comedy_club import ComedyClub
    from .models.comedy_event import ComedyEvent
    from .models.comic_cover_art import ComicCoverArt
    from .models.comic_issue import ComicIssue
    from .models.comic_series import ComicSeries
    from .models.comic_story import ComicStory
    from .models.comment import Comment
    from .models.comment_action import CommentAction
    from .models.communicate_action import CommunicateAction
    from .models.complete_data_feed import CompleteDataFeed
    from .models.compound_price_specification import CompoundPriceSpecification
    from .models.computer_language import ComputerLanguage
    from .models.computer_store import ComputerStore
    from .models.conference_event import ConferenceEvent
    from .models.confirm_action import ConfirmAction
    from .models.consortium import Consortium
    from .models.constraint_node import ConstraintNode
    from .models.consume_action import ConsumeAction
    from .models.contact_page import ContactPage
    from .models.contact_point import ContactPoint
    from .models.contact_point_option import ContactPointOption
    from .models.continent import Continent
    from .models.control_action import ControlAction
    from .models.convenience_store import ConvenienceStore
    from .models.conversation import Conversation
    from .models.cook_action import CookAction
    from .models.cooperative import Cooperative
    from .models.corporation import Corporation
    from .models.correction_comment import CorrectionComment
    from .models.country import Country
    from .models.course import Course
    from .models.course_instance import CourseInstance
    from .models.courthouse import Courthouse
    from .models.cover_art import CoverArt
    from .models.covid_testing_facility import CovidTestingFacility
    from .models.create_action import CreateAction
    from .models.creative_work import CreativeWork
    from .models.creative_work_season import CreativeWorkSeason
    from .models.creative_work_series import CreativeWorkSeries
    from .models.credential import Credential
    from .models.credit_card import CreditCard
    from .models.crematorium import Crematorium
    from .models.critic_review import CriticReview
    from .models.currency_conversion_service import CurrencyConversionService
    from .models.d_dx_element import DDxElement
    from .models.de_nonprofit_type import DENonprofitType
    from .models.dance_event import DanceEvent
    from .models.dance_group import DanceGroup
    from .models.data_catalog import DataCatalog
    from .models.data_download import DataDownload
    from .models.data_feed import DataFeed
    from .models.data_feed_item import DataFeedItem
    from .models.data_type import DataType
    from .models.dataset import Dataset
    from .models.day_of_week import DayOfWeek
    from .models.day_spa import DaySpa
    from .models.deactivate_action import DeactivateAction
    from .models.declaration_of_conformity import DeclarationOfConformity
    from .models.defence_establishment import DefenceEstablishment
    from .models.defined_region import DefinedRegion
    from .models.defined_term import DefinedTerm
    from .models.defined_term_set import DefinedTermSet
    from .models.delete_action import DeleteAction
    from .models.delivery_charge_specification import DeliveryChargeSpecification
    from .models.delivery_event import DeliveryEvent
    from .models.delivery_method import DeliveryMethod
    from .models.demand import Demand
    from .models.dentist import Dentist
    from .models.depart_action import DepartAction
    from .models.department_store import DepartmentStore
    from .models.deposit_account import DepositAccount
    from .models.diagnostic_lab import DiagnosticLab
    from .models.diagnostic_procedure import DiagnosticProcedure
    from .models.diet import Diet
    from .models.dietary_supplement import DietarySupplement
    from .models.digital_document import DigitalDocument
    from .models.digital_document_permission import DigitalDocumentPermission
    from .models.digital_document_permission_type import DigitalDocumentPermissionType
    from .models.digital_platform_enumeration import DigitalPlatformEnumeration
    from .models.digital_product_passport import DigitalProductPassport
    from .models.disagree_action import DisagreeAction
    from .models.discover_action import DiscoverAction
    from .models.discussion_forum_posting import DiscussionForumPosting
    from .models.dislike_action import DislikeAction
    from .models.distillery import Distillery
    from .models.donate_action import DonateAction
    from .models.dose_schedule import DoseSchedule
    from .models.download_action import DownloadAction
    from .models.draw_action import DrawAction
    from .models.drawing import Drawing
    from .models.drink_action import DrinkAction
    from .models.drive_wheel_configuration_value import DriveWheelConfigurationValue
    from .models.drug import Drug
    from .models.drug_class import DrugClass
    from .models.drug_cost import DrugCost
    from .models.drug_cost_category import DrugCostCategory
    from .models.drug_legal_status import DrugLegalStatus
    from .models.drug_pregnancy_category import DrugPregnancyCategory
    from .models.drug_prescription_status import DrugPrescriptionStatus
    from .models.drug_strength import DrugStrength
    from .models.dry_cleaning_or_laundry import DryCleaningOrLaundry
    from .models.eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
    from .models.eat_action import EatAction
    from .models.education_event import EducationEvent
    from .models.educational_audience import EducationalAudience
    from .models.educational_occupational_credential import EducationalOccupationalCredential
    from .models.educational_occupational_program import EducationalOccupationalProgram
    from .models.educational_organization import EducationalOrganization
    from .models.electrician import Electrician
    from .models.electronics_store import ElectronicsStore
    from .models.elementary_school import ElementarySchool
    from .models.email_message import EmailMessage
    from .models.embassy import Embassy
    from .models.emergency_service import EmergencyService
    from .models.employee_role import EmployeeRole
    from .models.employer_aggregate_rating import EmployerAggregateRating
    from .models.employer_review import EmployerReview
    from .models.employment_agency import EmploymentAgency
    from .models.endorse_action import EndorseAction
    from .models.endorsement_rating import EndorsementRating
    from .models.energy_consumption_details import EnergyConsumptionDetails
    from .models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration
    from .models.energy_star_energy_efficiency_enumeration import EnergyStarEnergyEfficiencyEnumeration
    from .models.engine_specification import EngineSpecification
    from .models.entertainment_business import EntertainmentBusiness
    from .models.entry_point import EntryPoint
    from .models.enumeration import Enumeration
    from .models.environmental_product_declaration import EnvironmentalProductDeclaration
    from .models.episode import Episode
    from .models.error import Error
    from .models.event import Event
    from .models.event_attendance_mode_enumeration import EventAttendanceModeEnumeration
    from .models.event_reservation import EventReservation
    from .models.event_series import EventSeries
    from .models.event_status_type import EventStatusType
    from .models.event_venue import EventVenue
    from .models.exchange_rate_specification import ExchangeRateSpecification
    from .models.exercise_action import ExerciseAction
    from .models.exercise_gym import ExerciseGym
    from .models.exercise_plan import ExercisePlan
    from .models.exhibition_event import ExhibitionEvent
    from .models.faq_page import FAQPage
    from .models.fm_radio_channel import FMRadioChannel
    from .models.fast_food_restaurant import FastFoodRestaurant
    from .models.festival import Festival
    from .models.film_action import FilmAction
    from .models.financial_incentive import FinancialIncentive
    from .models.financial_product import FinancialProduct
    from .models.financial_service import FinancialService
    from .models.find_action import FindAction
    from .models.fire_station import FireStation
    from .models.flight import Flight
    from .models.flight_reservation import FlightReservation
    from .models.floor_plan import FloorPlan
    from .models.florist import Florist
    from .models.follow_action import FollowAction
    from .models.food_establishment import FoodEstablishment
    from .models.food_establishment_reservation import FoodEstablishmentReservation
    from .models.food_event import FoodEvent
    from .models.food_service import FoodService
    from .models.fulfillment_type_enumeration import FulfillmentTypeEnumeration
    from .models.funding_agency import FundingAgency
    from .models.funding_scheme import FundingScheme
    from .models.furniture_store import FurnitureStore
    from .models.game import Game
    from .models.game_availability_enumeration import GameAvailabilityEnumeration
    from .models.game_play_mode import GamePlayMode
    from .models.game_server import GameServer
    from .models.game_server_status import GameServerStatus
    from .models.garden_store import GardenStore
    from .models.gas_station import GasStation
    from .models.gated_residence_community import GatedResidenceCommunity
    from .models.gender_type import GenderType
    from .models.gene import Gene
    from .models.general_contractor import GeneralContractor
    from .models.geo_circle import GeoCircle
    from .models.geo_coordinates import GeoCoordinates
    from .models.geo_shape import GeoShape
    from .models.geospatial_geometry import GeospatialGeometry
    from .models.give_action import GiveAction
    from .models.golf_course import GolfCourse
    from .models.government_benefits_type import GovernmentBenefitsType
    from .models.government_building import GovernmentBuilding
    from .models.government_office import GovernmentOffice
    from .models.government_organization import GovernmentOrganization
    from .models.government_permit import GovernmentPermit
    from .models.government_service import GovernmentService
    from .models.grant import Grant
    from .models.grocery_store import GroceryStore
    from .models.guide import Guide
    from .models.hvac_business import HVACBusiness
    from .models.hackathon import Hackathon
    from .models.hair_salon import HairSalon
    from .models.hardware_store import HardwareStore
    from .models.health_and_beauty_business import HealthAndBeautyBusiness
    from .models.health_aspect_enumeration import HealthAspectEnumeration
    from .models.health_club import HealthClub
    from .models.health_insurance_plan import HealthInsurancePlan
    from .models.health_plan_cost_sharing_specification import HealthPlanCostSharingSpecification
    from .models.health_plan_formulary import HealthPlanFormulary
    from .models.health_plan_network import HealthPlanNetwork
    from .models.health_topic_content import HealthTopicContent
    from .models.high_school import HighSchool
    from .models.hindu_temple import HinduTemple
    from .models.hobby_shop import HobbyShop
    from .models.home_and_construction_business import HomeAndConstructionBusiness
    from .models.home_goods_store import HomeGoodsStore
    from .models.hospital import Hospital
    from .models.hostel import Hostel
    from .models.hotel import Hotel
    from .models.hotel_room import HotelRoom
    from .models.house import House
    from .models.house_painter import HousePainter
    from .models.how_to import HowTo
    from .models.how_to_direction import HowToDirection
    from .models.how_to_item import HowToItem
    from .models.how_to_section import HowToSection
    from .models.how_to_step import HowToStep
    from .models.how_to_supply import HowToSupply
    from .models.how_to_tip import HowToTip
    from .models.how_to_tool import HowToTool
    from .models.hyper_toc import HyperToc
    from .models.hyper_toc_entry import HyperTocEntry
    from .models.iptc_digital_source_enumeration import IPTCDigitalSourceEnumeration
    from .models.it_nonprofit_type import ITNonprofitType
    from .models.ice_cream_shop import IceCreamShop
    from .models.ignore_action import IgnoreAction
    from .models.image_gallery import ImageGallery
    from .models.image_object import ImageObject
    from .models.image_object_snapshot import ImageObjectSnapshot
    from .models.imaging_test import ImagingTest
    from .models.incentive_qualified_expense_type import IncentiveQualifiedExpenseType
    from .models.incentive_status import IncentiveStatus
    from .models.incentive_type import IncentiveType
    from .models.individual_physician import IndividualPhysician
    from .models.individual_product import IndividualProduct
    from .models.infectious_agent_class import InfectiousAgentClass
    from .models.infectious_disease import InfectiousDisease
    from .models.inform_action import InformAction
    from .models.insert_action import InsertAction
    from .models.install_action import InstallAction
    from .models.instantaneous_event import InstantaneousEvent
    from .models.insurance_agency import InsuranceAgency
    from .models.intangible import Intangible
    from .models.interact_action import InteractAction
    from .models.interaction_counter import InteractionCounter
    from .models.internet_cafe import InternetCafe
    from .models.investment_fund import InvestmentFund
    from .models.investment_or_deposit import InvestmentOrDeposit
    from .models.invite_action import InviteAction
    from .models.invoice import Invoice
    from .models.item_availability import ItemAvailability
    from .models.item_list import ItemList
    from .models.item_list_order_type import ItemListOrderType
    from .models.item_page import ItemPage
    from .models.jewelry_store import JewelryStore
    from .models.job_posting import JobPosting
    from .models.join_action import JoinAction
    from .models.joint import Joint
    from .models.lake_body_of_water import LakeBodyOfWater
    from .models.landform import Landform
    from .models.landmarks_or_historical_buildings import LandmarksOrHistoricalBuildings
    from .models.language import Language
    from .models.learning_resource import LearningResource
    from .models.leave_action import LeaveAction
    from .models.legal_force_status import LegalForceStatus
    from .models.legal_service import LegalService
    from .models.legal_value_level import LegalValueLevel
    from .models.legislation import Legislation
    from .models.legislation_object import LegislationObject
    from .models.legislative_building import LegislativeBuilding
    from .models.lend_action import LendAction
    from .models.library import Library
    from .models.library_system import LibrarySystem
    from .models.lifestyle_modification import LifestyleModification
    from .models.ligament import Ligament
    from .models.like_action import LikeAction
    from .models.link_role import LinkRole
    from .models.liquor_store import LiquorStore
    from .models.list_item import ListItem
    from .models.listen_action import ListenAction
    from .models.literary_event import LiteraryEvent
    from .models.live_blog_posting import LiveBlogPosting
    from .models.loan_or_credit import LoanOrCredit
    from .models.local_business import LocalBusiness
    from .models.location_feature_specification import LocationFeatureSpecification
    from .models.locksmith import Locksmith
    from .models.lodging_business import LodgingBusiness
    from .models.lodging_reservation import LodgingReservation
    from .models.login_action import LoginAction
    from .models.lose_action import LoseAction
    from .models.lymphatic_vessel import LymphaticVessel
    from .models.manuscript import Manuscript
    from .models.map import Map
    from .models.map_category_type import MapCategoryType
    from .models.marry_action import MarryAction
    from .models.math_solver import MathSolver
    from .models.maximum_dose_schedule import MaximumDoseSchedule
    from .models.measurement_method_enum import MeasurementMethodEnum
    from .models.measurement_type_enumeration import MeasurementTypeEnumeration
    from .models.media_enumeration import MediaEnumeration
    from .models.media_gallery import MediaGallery
    from .models.media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration
    from .models.media_object import MediaObject
    from .models.media_review import MediaReview
    from .models.media_review_item import MediaReviewItem
    from .models.media_subscription import MediaSubscription
    from .models.medical_audience import MedicalAudience
    from .models.medical_audience_type import MedicalAudienceType
    from .models.medical_business import MedicalBusiness
    from .models.medical_cause import MedicalCause
    from .models.medical_clinic import MedicalClinic
    from .models.medical_code import MedicalCode
    from .models.medical_condition import MedicalCondition
    from .models.medical_condition_stage import MedicalConditionStage
    from .models.medical_contraindication import MedicalContraindication
    from .models.medical_device import MedicalDevice
    from .models.medical_device_purpose import MedicalDevicePurpose
    from .models.medical_entity import MedicalEntity
    from .models.medical_enumeration import MedicalEnumeration
    from .models.medical_evidence_level import MedicalEvidenceLevel
    from .models.medical_guideline import MedicalGuideline
    from .models.medical_guideline_contraindication import MedicalGuidelineContraindication
    from .models.medical_guideline_recommendation import MedicalGuidelineRecommendation
    from .models.medical_imaging_technique import MedicalImagingTechnique
    from .models.medical_indication import MedicalIndication
    from .models.medical_intangible import MedicalIntangible
    from .models.medical_observational_study import MedicalObservationalStudy
    from .models.medical_observational_study_design import MedicalObservationalStudyDesign
    from .models.medical_organization import MedicalOrganization
    from .models.medical_procedure import MedicalProcedure
    from .models.medical_procedure_type import MedicalProcedureType
    from .models.medical_risk_calculator import MedicalRiskCalculator
    from .models.medical_risk_estimator import MedicalRiskEstimator
    from .models.medical_risk_factor import MedicalRiskFactor
    from .models.medical_risk_score import MedicalRiskScore
    from .models.medical_scholarly_article import MedicalScholarlyArticle
    from .models.medical_sign import MedicalSign
    from .models.medical_sign_or_symptom import MedicalSignOrSymptom
    from .models.medical_specialty import MedicalSpecialty
    from .models.medical_study import MedicalStudy
    from .models.medical_study_status import MedicalStudyStatus
    from .models.medical_symptom import MedicalSymptom
    from .models.medical_test import MedicalTest
    from .models.medical_test_panel import MedicalTestPanel
    from .models.medical_therapy import MedicalTherapy
    from .models.medical_trial import MedicalTrial
    from .models.medical_trial_design import MedicalTrialDesign
    from .models.medical_web_page import MedicalWebPage
    from .models.medicine_system import MedicineSystem
    from .models.meeting_room import MeetingRoom
    from .models.member_program import MemberProgram
    from .models.member_program_tier import MemberProgramTier
    from .models.mens_clothing_store import MensClothingStore
    from .models.menu import Menu
    from .models.menu_item import MenuItem
    from .models.menu_section import MenuSection
    from .models.merchant_return_enumeration import MerchantReturnEnumeration
    from .models.merchant_return_policy import MerchantReturnPolicy
    from .models.merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .models.message import Message
    from .models.middle_school import MiddleSchool
    from .models.mobile_application import MobileApplication
    from .models.mobile_phone_store import MobilePhoneStore
    from .models.molecular_entity import MolecularEntity
    from .models.monetary_amount import MonetaryAmount
    from .models.monetary_amount_distribution import MonetaryAmountDistribution
    from .models.monetary_grant import MonetaryGrant
    from .models.money_transfer import MoneyTransfer
    from .models.mortgage_loan import MortgageLoan
    from .models.mosque import Mosque
    from .models.motel import Motel
    from .models.motorcycle import Motorcycle
    from .models.motorcycle_dealer import MotorcycleDealer
    from .models.motorcycle_repair import MotorcycleRepair
    from .models.motorized_bicycle import MotorizedBicycle
    from .models.mountain import Mountain
    from .models.move_action import MoveAction
    from .models.movie import Movie
    from .models.movie_clip import MovieClip
    from .models.movie_rental_store import MovieRentalStore
    from .models.movie_series import MovieSeries
    from .models.movie_theater import MovieTheater
    from .models.moving_company import MovingCompany
    from .models.muscle import Muscle
    from .models.museum import Museum
    from .models.music_album import MusicAlbum
    from .models.music_album_production_type import MusicAlbumProductionType
    from .models.music_album_release_type import MusicAlbumReleaseType
    from .models.music_composition import MusicComposition
    from .models.music_event import MusicEvent
    from .models.music_group import MusicGroup
    from .models.music_playlist import MusicPlaylist
    from .models.music_recording import MusicRecording
    from .models.music_release import MusicRelease
    from .models.music_release_format_type import MusicReleaseFormatType
    from .models.music_store import MusicStore
    from .models.music_venue import MusicVenue
    from .models.music_video_object import MusicVideoObject
    from .models.ngo import NGO
    from .models.nl_nonprofit_type import NLNonprofitType
    from .models.nail_salon import NailSalon
    from .models.nerve import Nerve
    from .models.news_article import NewsArticle
    from .models.news_media_organization import NewsMediaOrganization
    from .models.newspaper import Newspaper
    from .models.night_club import NightClub
    from .models.nonprofit_type import NonprofitType
    from .models.notary import Notary
    from .models.note_digital_document import NoteDigitalDocument
    from .models.nutrition_information import NutritionInformation
    from .models.observation import Observation
    from .models.occupation import Occupation
    from .models.occupational_experience_requirements import OccupationalExperienceRequirements
    from .models.occupational_therapy import OccupationalTherapy
    from .models.ocean_body_of_water import OceanBodyOfWater
    from .models.offer import Offer
    from .models.offer_catalog import OfferCatalog
    from .models.offer_for_lease import OfferForLease
    from .models.offer_for_purchase import OfferForPurchase
    from .models.offer_item_condition import OfferItemCondition
    from .models.offer_shipping_details import OfferShippingDetails
    from .models.office_equipment_store import OfficeEquipmentStore
    from .models.on_demand_event import OnDemandEvent
    from .models.online_business import OnlineBusiness
    from .models.online_marketplace import OnlineMarketplace
    from .models.online_store import OnlineStore
    from .models.opening_hours_specification import OpeningHoursSpecification
    from .models.operating_system import OperatingSystem
    from .models.opinion_news_article import OpinionNewsArticle
    from .models.optician import Optician
    from .models.order import Order
    from .models.order_action import OrderAction
    from .models.order_item import OrderItem
    from .models.order_status import OrderStatus
    from .models.organization import Organization
    from .models.organization_role import OrganizationRole
    from .models.organize_action import OrganizeAction
    from .models.outlet_store import OutletStore
    from .models.ownership_info import OwnershipInfo
    from .models.paint_action import PaintAction
    from .models.painting import Painting
    from .models.palliative_procedure import PalliativeProcedure
    from .models.parcel_delivery import ParcelDelivery
    from .models.parent_audience import ParentAudience
    from .models.park import Park
    from .models.parking_facility import ParkingFacility
    from .models.pathology_test import PathologyTest
    from .models.patient import Patient
    from .models.pawn_shop import PawnShop
    from .models.pay_action import PayAction
    from .models.payment_card import PaymentCard
    from .models.payment_charge_specification import PaymentChargeSpecification
    from .models.payment_method import PaymentMethod
    from .models.payment_method_type import PaymentMethodType
    from .models.payment_service import PaymentService
    from .models.payment_status_type import PaymentStatusType
    from .models.people_audience import PeopleAudience
    from .models.perform_action import PerformAction
    from .models.performance_role import PerformanceRole
    from .models.performing_arts_event import PerformingArtsEvent
    from .models.performing_arts_theater import PerformingArtsTheater
    from .models.performing_group import PerformingGroup
    from .models.periodical import Periodical
    from .models.permit import Permit
    from .models.person import Person
    from .models.pet_store import PetStore
    from .models.pharmacy import Pharmacy
    from .models.photograph import Photograph
    from .models.photograph_action import PhotographAction
    from .models.physical_activity import PhysicalActivity
    from .models.physical_activity_category import PhysicalActivityCategory
    from .models.physical_exam import PhysicalExam
    from .models.physical_therapy import PhysicalTherapy
    from .models.physician import Physician
    from .models.physicians_office import PhysiciansOffice
    from .models.place import Place
    from .models.place_of_worship import PlaceOfWorship
    from .models.plan_action import PlanAction
    from .models.play import Play
    from .models.play_action import PlayAction
    from .models.play_game_action import PlayGameAction
    from .models.playground import Playground
    from .models.plumber import Plumber
    from .models.podcast_episode import PodcastEpisode
    from .models.podcast_season import PodcastSeason
    from .models.podcast_series import PodcastSeries
    from .models.police_station import PoliceStation
    from .models.political_party import PoliticalParty
    from .models.pond import Pond
    from .models.post_office import PostOffice
    from .models.postal_address import PostalAddress
    from .models.postal_code_range_specification import PostalCodeRangeSpecification
    from .models.poster import Poster
    from .models.pre_order_action import PreOrderAction
    from .models.prepend_action import PrependAction
    from .models.preschool import Preschool
    from .models.presentation_digital_document import PresentationDigitalDocument
    from .models.prevention_indication import PreventionIndication
    from .models.price_component_type_enumeration import PriceComponentTypeEnumeration
    from .models.price_specification import PriceSpecification
    from .models.price_type_enumeration import PriceTypeEnumeration
    from .models.product import Product
    from .models.product_collection import ProductCollection
    from .models.product_group import ProductGroup
    from .models.product_model import ProductModel
    from .models.professional_service import ProfessionalService
    from .models.profile_page import ProfilePage
    from .models.program_membership import ProgramMembership
    from .models.project import Project
    from .models.property import Property
    from .models.property_value import PropertyValue
    from .models.property_value_specification import PropertyValueSpecification
    from .models.protein import Protein
    from .models.psychological_treatment import PsychologicalTreatment
    from .models.public_swimming_pool import PublicSwimmingPool
    from .models.public_toilet import PublicToilet
    from .models.publication_event import PublicationEvent
    from .models.publication_issue import PublicationIssue
    from .models.publication_volume import PublicationVolume
    from .models.purchase_type import PurchaseType
    from .models.qa_page import QAPage
    from .models.qualitative_value import QualitativeValue
    from .models.quantitative_value import QuantitativeValue
    from .models.quantitative_value_distribution import QuantitativeValueDistribution
    from .models.question import Question
    from .models.quiz import Quiz
    from .models.quotation import Quotation
    from .models.quote_action import QuoteAction
    from .models.rv_park import RVPark
    from .models.radiation_therapy import RadiationTherapy
    from .models.radio_broadcast_service import RadioBroadcastService
    from .models.radio_channel import RadioChannel
    from .models.radio_clip import RadioClip
    from .models.radio_episode import RadioEpisode
    from .models.radio_season import RadioSeason
    from .models.radio_series import RadioSeries
    from .models.radio_station import RadioStation
    from .models.rating import Rating
    from .models.react_action import ReactAction
    from .models.read_action import ReadAction
    from .models.real_estate_agent import RealEstateAgent
    from .models.real_estate_listing import RealEstateListing
    from .models.receive_action import ReceiveAction
    from .models.recipe import Recipe
    from .models.recommendation import Recommendation
    from .models.recommended_dose_schedule import RecommendedDoseSchedule
    from .models.recycling_center import RecyclingCenter
    from .models.refund_type_enumeration import RefundTypeEnumeration
    from .models.register_action import RegisterAction
    from .models.reject_action import RejectAction
    from .models.rent_action import RentAction
    from .models.rental_car_reservation import RentalCarReservation
    from .models.repayment_specification import RepaymentSpecification
    from .models.replace_action import ReplaceAction
    from .models.reply_action import ReplyAction
    from .models.report import Report
    from .models.reportage_news_article import ReportageNewsArticle
    from .models.reported_dose_schedule import ReportedDoseSchedule
    from .models.research_organization import ResearchOrganization
    from .models.research_project import ResearchProject
    from .models.researcher import Researcher
    from .models.reservation import Reservation
    from .models.reservation_package import ReservationPackage
    from .models.reservation_status_type import ReservationStatusType
    from .models.reserve_action import ReserveAction
    from .models.reservoir import Reservoir
    from .models.reset_password_action import ResetPasswordAction
    from .models.residence import Residence
    from .models.resort import Resort
    from .models.restaurant import Restaurant
    from .models.restricted_diet import RestrictedDiet
    from .models.resume_action import ResumeAction
    from .models.return_action import ReturnAction
    from .models.return_fees_enumeration import ReturnFeesEnumeration
    from .models.return_label_source_enumeration import ReturnLabelSourceEnumeration
    from .models.return_method_enumeration import ReturnMethodEnumeration
    from .models.review import Review
    from .models.review_action import ReviewAction
    from .models.review_news_article import ReviewNewsArticle
    from .models.river_body_of_water import RiverBodyOfWater
    from .models.role import Role
    from .models.roofing_contractor import RoofingContractor
    from .models.room import Room
    from .models.rsvp_action import RsvpAction
    from .models.rsvp_response_type import RsvpResponseType
    from .models.runtime_platform import RuntimePlatform
    from .models.sale_event import SaleEvent
    from .models.satirical_article import SatiricalArticle
    from .models.schedule import Schedule
    from .models.schedule_action import ScheduleAction
    from .models.scholarly_article import ScholarlyArticle
    from .models.school import School
    from .models.school_district import SchoolDistrict
    from .models.screening_event import ScreeningEvent
    from .models.sculpture import Sculpture
    from .models.sea_body_of_water import SeaBodyOfWater
    from .models.search_action import SearchAction
    from .models.search_rescue_organization import SearchRescueOrganization
    from .models.search_results_page import SearchResultsPage
    from .models.seat import Seat
    from .models.seek_to_action import SeekToAction
    from .models.self_storage import SelfStorage
    from .models.sell_action import SellAction
    from .models.send_action import SendAction
    from .models.sequential_art import SequentialArt
    from .models.series import Series
    from .models.service import Service
    from .models.service_channel import ServiceChannel
    from .models.service_period import ServicePeriod
    from .models.share_action import ShareAction
    from .models.sheet_music import SheetMusic
    from .models.shipping_conditions import ShippingConditions
    from .models.shipping_delivery_time import ShippingDeliveryTime
    from .models.shipping_rate_settings import ShippingRateSettings
    from .models.shipping_service import ShippingService
    from .models.shoe_store import ShoeStore
    from .models.shopping_center import ShoppingCenter
    from .models.short_story import ShortStory
    from .models.single_family_residence import SingleFamilyResidence
    from .models.site_navigation_element import SiteNavigationElement
    from .models.size_group_enumeration import SizeGroupEnumeration
    from .models.size_specification import SizeSpecification
    from .models.size_system_enumeration import SizeSystemEnumeration
    from .models.ski_resort import SkiResort
    from .models.social_event import SocialEvent
    from .models.social_media_posting import SocialMediaPosting
    from .models.software_application import SoftwareApplication
    from .models.software_source_code import SoftwareSourceCode
    from .models.solve_math_action import SolveMathAction
    from .models.some_products import SomeProducts
    from .models.speakable_specification import SpeakableSpecification
    from .models.special_announcement import SpecialAnnouncement
    from .models.specialty import Specialty
    from .models.sporting_goods_store import SportingGoodsStore
    from .models.sports_activity_location import SportsActivityLocation
    from .models.sports_club import SportsClub
    from .models.sports_event import SportsEvent
    from .models.sports_organization import SportsOrganization
    from .models.sports_team import SportsTeam
    from .models.spreadsheet_digital_document import SpreadsheetDigitalDocument
    from .models.stadium_or_arena import StadiumOrArena
    from .models.state import State
    from .models.statement import Statement
    from .models.statistical_population import StatisticalPopulation
    from .models.statistical_variable import StatisticalVariable
    from .models.status_enumeration import StatusEnumeration
    from .models.steering_position_value import SteeringPositionValue
    from .models.store import Store
    from .models.structured_value import StructuredValue
    from .models.subscribe_action import SubscribeAction
    from .models.substance import Substance
    from .models.subway_station import SubwayStation
    from .models.suite import Suite
    from .models.superficial_anatomy import SuperficialAnatomy
    from .models.surgical_procedure import SurgicalProcedure
    from .models.suspend_action import SuspendAction
    from .models.syllabus import Syllabus
    from .models.synagogue import Synagogue
    from .models.tv_clip import TVClip
    from .models.tv_episode import TVEpisode
    from .models.tv_season import TVSeason
    from .models.tv_series import TVSeries
    from .models.table import Table
    from .models.take_action import TakeAction
    from .models.tattoo_parlor import TattooParlor
    from .models.taxi_reservation import TaxiReservation
    from .models.taxi_service import TaxiService
    from .models.taxi_stand import TaxiStand
    from .models.taxon import Taxon
    from .models.tech_article import TechArticle
    from .models.television_channel import TelevisionChannel
    from .models.television_station import TelevisionStation
    from .models.tennis_complex import TennisComplex
    from .models.text_digital_document import TextDigitalDocument
    from .models.text_object import TextObject
    from .models.theater_event import TheaterEvent
    from .models.theater_group import TheaterGroup
    from .models.therapeutic_procedure import TherapeuticProcedure
    from .models.thesis import Thesis
    from .models.thing import Thing
    from .models.three_d_model import ThreeDModel
    from .models.ticket import Ticket
    from .models.tie_action import TieAction
    from .models.tier_benefit_enumeration import TierBenefitEnumeration
    from .models.tip_action import TipAction
    from .models.tire_shop import TireShop
    from .models.tourist_attraction import TouristAttraction
    from .models.tourist_destination import TouristDestination
    from .models.tourist_information_center import TouristInformationCenter
    from .models.tourist_trip import TouristTrip
    from .models.toy_store import ToyStore
    from .models.track_action import TrackAction
    from .models.trade_action import TradeAction
    from .models.train_reservation import TrainReservation
    from .models.train_station import TrainStation
    from .models.train_trip import TrainTrip
    from .models.transfer_action import TransferAction
    from .models.travel_action import TravelAction
    from .models.travel_agency import TravelAgency
    from .models.treatment_indication import TreatmentIndication
    from .models.trip import Trip
    from .models.type_and_quantity_node import TypeAndQuantityNode
    from .models.uk_nonprofit_type import UKNonprofitType
    from .models.us_nonprofit_type import USNonprofitType
    from .models.un_register_action import UnRegisterAction
    from .models.unit_price_specification import UnitPriceSpecification
    from .models.update_action import UpdateAction
    from .models.use_action import UseAction
    from .models.user_review import UserReview
    from .models.vacation_rental import VacationRental
    from .models.vehicle import Vehicle
    from .models.vein import Vein
    from .models.vessel import Vessel
    from .models.veterinary_care import VeterinaryCare
    from .models.video_gallery import VideoGallery
    from .models.video_game import VideoGame
    from .models.video_game_clip import VideoGameClip
    from .models.video_game_series import VideoGameSeries
    from .models.video_object import VideoObject
    from .models.video_object_snapshot import VideoObjectSnapshot
    from .models.view_action import ViewAction
    from .models.virtual_location import VirtualLocation
    from .models.visual_arts_event import VisualArtsEvent
    from .models.visual_artwork import VisualArtwork
    from .models.vital_sign import VitalSign
    from .models.volcano import Volcano
    from .models.vote_action import VoteAction
    from .models.wp_ad_block import WPAdBlock
    from .models.wp_footer import WPFooter
    from .models.wp_header import WPHeader
    from .models.wp_side_bar import WPSideBar
    from .models.want_action import WantAction
    from .models.warranty_promise import WarrantyPromise
    from .models.warranty_scope import WarrantyScope
    from .models.watch_action import WatchAction
    from .models.waterfall import Waterfall
    from .models.wear_action import WearAction
    from .models.wearable_measurement_type_enumeration import WearableMeasurementTypeEnumeration
    from .models.wearable_size_group_enumeration import WearableSizeGroupEnumeration
    from .models.wearable_size_system_enumeration import WearableSizeSystemEnumeration
    from .models.web_api import WebAPI
    from .models.web_application import WebApplication
    from .models.web_content import WebContent
    from .models.web_page import WebPage
    from .models.web_page_element import WebPageElement
    from .models.web_site import WebSite
    from .models.wholesale_store import WholesaleStore
    from .models.win_action import WinAction
    from .models.winery import Winery
    from .models.work_based_program import WorkBasedProgram
    from .models.workers_union import WorkersUnion
    from .models.write_action import WriteAction
    from .models.zoo import Zoo
