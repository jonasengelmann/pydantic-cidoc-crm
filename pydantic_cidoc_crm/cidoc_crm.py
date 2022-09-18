from __future__ import annotations

from typing import List, Optional, Union

from .abstract_basemodel import AbstractBaseModel
from .mapping import mapping


class RDFBaseModel(AbstractBaseModel):
    _mapping = mapping


class E1CRMEntity(RDFBaseModel):
    p01i_is_domain_of: Optional[
        Union[List[PC0TypedCRMProperty], PC0TypedCRMProperty]
    ] = None
    p02i_is_range_of: Optional[
        Union[List[PC0TypedCRMProperty], PC0TypedCRMProperty]
    ] = None
    p129i_is_subject_of: Optional[
        Union[List[E89PropositionalObject], E89PropositionalObject]
    ] = None
    p136i_supported_type_creation: Optional[
        Union[List[E83TypeCreation], E83TypeCreation]
    ] = None
    p137_exemplifies: Optional[Union[List[E55Type], E55Type]] = None
    p138i_has_representation: Optional[Union[List[E36VisualItem], E36VisualItem]] = None
    p140i_was_attributed_by: Optional[
        Union[List[E13AttributeAssignment], E13AttributeAssignment]
    ] = None
    p141i_was_assigned_by: Optional[
        Union[List[E13AttributeAssignment], E13AttributeAssignment]
    ] = None
    p15i_influenced: Optional[Union[List[E7Activity], E7Activity]] = None
    p17i_motivated: Optional[Union[List[E7Activity], E7Activity]] = None
    p1_is_identified_by: Optional[Union[List[E41Appellation], E41Appellation]] = None
    p2_has_type: Optional[Union[List[E55Type], E55Type]] = None
    p3_has_note: Optional[Union[List[str], str]] = None
    p41i_was_classified_by: Optional[
        Union[List[E17TypeAssignment], E17TypeAssignment]
    ] = None
    p48_has_preferred_identifier: Optional[
        Union[List[E42Identifier], E42Identifier]
    ] = None
    p62i_is_depicted_by: Optional[
        Union[List[E24PhysicalHumanMadeThing], E24PhysicalHumanMadeThing]
    ] = None
    p67i_is_referred_to_by: Optional[
        Union[List[E89PropositionalObject], E89PropositionalObject]
    ] = None
    p70i_is_documented_in: Optional[Union[List[E31Document], E31Document]] = None
    p71i_is_listed_in: Optional[
        Union[List[E32AuthorityDocument], E32AuthorityDocument]
    ] = None


class PC0TypedCRMProperty(RDFBaseModel):
    p01_has_domain: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p02_has_range: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p03_has_range_literal: Optional[Union[List[str], str]] = None


class E2TemporalEntity(E1CRMEntity):
    p173_starts_before_or_with_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p173i_ends_after_or_with_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p174_starts_before_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p174i_ends_after_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p175_starts_before_or_with_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p175i_starts_after_or_with_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p176_starts_before_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p176i_starts_after_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p182_ends_before_or_with_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p182i_starts_after_or_with_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p183_ends_before_the_start_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p183i_starts_after_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p184_ends_before_or_with_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p184i_ends_with_or_after_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p185_ends_before_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p185i_ends_after_the_end_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p4_has_time_span: Optional[Union[List[E52TimeSpan], E52TimeSpan]] = None


class E52TimeSpan(E1CRMEntity):
    p160i_is_temporal_projection_of: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p164i_temporally_specifies: Optional[Union[List[E93Presence], E93Presence]] = None
    p170i_time_is_defined_by: Optional[Union[List[str], str]] = None
    p191_had_duration: Optional[Union[List[E54Dimension], E54Dimension]] = None
    p4i_is_time_span_of: Optional[
        Union[List[E2TemporalEntity], E2TemporalEntity]
    ] = None
    p79_beginning_is_qualified_by: Optional[Union[List[str], str]] = None
    p80_end_is_qualified_by: Optional[Union[List[str], str]] = None
    p81_ongoing_throughout: Optional[Union[List[str], str]] = None
    p81a_end_of_the_begin: Optional[Union[List[str], str]] = None
    p81b_begin_of_the_end: Optional[Union[List[str], str]] = None
    p82_at_some_time_within: Optional[Union[List[str], str]] = None
    p82a_begin_of_the_begin: Optional[Union[List[str], str]] = None
    p82b_end_of_the_end: Optional[Union[List[str], str]] = None
    p86_falls_within: Optional[Union[List[E52TimeSpan], E52TimeSpan]] = None
    p86i_contains: Optional[Union[List[E52TimeSpan], E52TimeSpan]] = None


class E53Place(E1CRMEntity):
    p121_overlaps_with: Optional[Union[List[E53Place], E53Place]] = None
    p122_borders_with: Optional[Union[List[E53Place], E53Place]] = None
    p156i_is_occupied_by: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p157_is_at_rest_relative_to: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p161i_is_spatial_projection_of: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p167i_includes: Optional[Union[List[E93Presence], E93Presence]] = None
    p168_place_is_defined_by: Optional[Union[List[str], str]] = None
    p171_at_some_place_within: Optional[Union[List[str], str]] = None
    p172_contains: Optional[Union[List[str], str]] = None
    p189_approximates: Optional[Union[List[E53Place], E53Place]] = None
    p189i_is_approximated_by: Optional[Union[List[E53Place], E53Place]] = None
    p197i_was_partially_covered_by: Optional[
        Union[List[E93Presence], E93Presence]
    ] = None
    p26i_was_destination_of: Optional[Union[List[E9Move], E9Move]] = None
    p27i_was_origin_of: Optional[Union[List[E9Move], E9Move]] = None
    p53i_is_former_or_current_location_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p54i_is_current_permanent_location_of: Optional[
        Union[List[E19PhysicalObject], E19PhysicalObject]
    ] = None
    p55i_currently_holds: Optional[
        Union[List[E19PhysicalObject], E19PhysicalObject]
    ] = None
    p59i_is_located_on_or_within: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p74i_is_current_or_former_residence_of: Optional[
        Union[List[E39Actor], E39Actor]
    ] = None
    p7i_witnessed: Optional[Union[List[E4Period], E4Period]] = None
    p89_falls_within: Optional[Union[List[E53Place], E53Place]] = None
    p89i_contains: Optional[Union[List[E53Place], E53Place]] = None


class E54Dimension(E1CRMEntity):
    p191i_was_duration_of: Optional[Union[List[E52TimeSpan], E52TimeSpan]] = None
    p40i_was_observed_in: Optional[Union[List[E16Measurement], E16Measurement]] = None
    p43i_is_dimension_of: Optional[Union[List[E70Thing], E70Thing]] = None
    p90_has_value: Optional[Union[List[str], str]] = None
    p90a_has_lower_value_limit: Optional[Union[List[str], str]] = None
    p90b_has_upper_value_limit: Optional[Union[List[str], str]] = None
    p91_has_unit: Optional[Union[List[E58MeasurementUnit], E58MeasurementUnit]] = None


class E77PersistentItem(E1CRMEntity):
    p12i_was_present_at: Optional[Union[List[E5Event], E5Event]] = None
    p92i_was_brought_into_existence_by: Optional[
        Union[List[E63BeginningofExistence], E63BeginningofExistence]
    ] = None
    p93i_was_taken_out_of_existence_by: Optional[
        Union[List[E64EndofExistence], E64EndofExistence]
    ] = None


class E92SpacetimeVolume(E1CRMEntity):
    p10_falls_within: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p10i_contains: Optional[Union[List[E92SpacetimeVolume], E92SpacetimeVolume]] = None
    p132_spatiotemporally_overlaps_with: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p133_is_spatiotemporally_separated_from: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p160_has_temporal_projection: Optional[Union[List[E52TimeSpan], E52TimeSpan]] = None
    p161_has_spatial_projection: Optional[Union[List[E53Place], E53Place]] = None
    p166i_had_presence: Optional[Union[List[E93Presence], E93Presence]] = None
    p169i_spacetime_volume_is_defined_by: Optional[Union[List[str], str]] = None
    p196i_is_defined_by: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None


class PC102hastitle(PC0TypedCRMProperty):
    p102_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class PC107hascurrentorformermember(PC0TypedCRMProperty):
    p107_1_kind_of_member: Optional[Union[List[E55Type], E55Type]] = None


class PC130showsfeaturesof(PC0TypedCRMProperty):
    p130_1_kind_of_similarity: Optional[Union[List[E55Type], E55Type]] = None


class PC136wasbasedon(PC0TypedCRMProperty):
    p136_1_in_the_taxonomic_role: Optional[Union[List[E55Type], E55Type]] = None


class PC137exemplifies(PC0TypedCRMProperty):
    p137_1_in_the_taxonomic_role: Optional[Union[List[E55Type], E55Type]] = None


class PC138represents(PC0TypedCRMProperty):
    p138_1_mode_of_representation: Optional[Union[List[E55Type], E55Type]] = None


class PC139hasalternativeform(PC0TypedCRMProperty):
    p139_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class PC144joinedwith(PC0TypedCRMProperty):
    p144_1_kind_of_member: Optional[Union[List[E55Type], E55Type]] = None


class PC14carriedoutby(PC0TypedCRMProperty):
    p14_1_in_the_role_of: Optional[Union[List[E55Type], E55Type]] = None


class PC16usedspecificobject(PC0TypedCRMProperty):
    p16_1_mode_of_use: Optional[Union[List[E55Type], E55Type]] = None


class PC189approximates(PC0TypedCRMProperty):
    p189_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class PC19wasintendeduseof(PC0TypedCRMProperty):
    p19_1_mode_of_use: Optional[Union[List[E55Type], E55Type]] = None


class PC3hasnote(PC0TypedCRMProperty):
    p3_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class PC62depicts(PC0TypedCRMProperty):
    p62_1_mode_of_depiction: Optional[Union[List[E55Type], E55Type]] = None


class PC67refersto(PC0TypedCRMProperty):
    p67_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class PC69hasassociationwith(PC0TypedCRMProperty):
    p69_1_has_type: Optional[Union[List[E55Type], E55Type]] = None


class E3ConditionState(E2TemporalEntity):
    p35i_was_identified_by: Optional[
        Union[List[E14ConditionAssessment], E14ConditionAssessment]
    ] = None
    p44i_is_condition_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p5_consists_of: Optional[Union[List[E3ConditionState], E3ConditionState]] = None
    p5i_forms_part_of: Optional[Union[List[E3ConditionState], E3ConditionState]] = None


class E4Period(E92SpacetimeVolume, E2TemporalEntity):
    p7_took_place_at: Optional[Union[List[E53Place], E53Place]] = None
    p8_took_place_on_or_within: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p9_consists_of: Optional[Union[List[E4Period], E4Period]] = None
    p9i_forms_part_of: Optional[Union[List[E4Period], E4Period]] = None


class E97MonetaryAmount(E54Dimension):
    p179i_was_sales_price_of: Optional[Union[List[E96Purchase], E96Purchase]] = None
    p180_has_currency: Optional[Union[List[E98Currency], E98Currency]] = None


class E39Actor(E77PersistentItem):
    p105i_has_right_on: Optional[Union[List[E72LegalObject], E72LegalObject]] = None
    p107i_is_current_or_former_member_of: Optional[
        Union[List[E74Group], E74Group]
    ] = None
    p109i_is_current_or_former_curator_of: Optional[
        Union[List[E78CuratedHolding], E78CuratedHolding]
    ] = None
    p11i_participated_in: Optional[Union[List[E5Event], E5Event]] = None
    p143i_was_joined_by: Optional[Union[List[E85Joining], E85Joining]] = None
    p145i_left_by: Optional[Union[List[E86Leaving], E86Leaving]] = None
    p14i_performed: Optional[Union[List[E7Activity], E7Activity]] = None
    p22i_acquired_title_through: Optional[
        Union[List[E8Acquisition], E8Acquisition]
    ] = None
    p23i_surrendered_title_through: Optional[
        Union[List[E8Acquisition], E8Acquisition]
    ] = None
    p28i_surrendered_custody_through: Optional[
        Union[List[E10TransferofCustody], E10TransferofCustody]
    ] = None
    p29i_received_custody_through: Optional[
        Union[List[E10TransferofCustody], E10TransferofCustody]
    ] = None
    p49i_is_former_or_current_keeper_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p50i_is_current_keeper_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p51i_is_former_or_current_owner_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p52i_is_current_owner_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p74_has_current_or_former_residence: Optional[
        Union[List[E53Place], E53Place]
    ] = None
    p75_possesses: Optional[Union[List[E30Right], E30Right]] = None
    p76_has_contact_point: Optional[Union[List[E41Appellation], E41Appellation]] = None


class E70Thing(E77PersistentItem):
    p101_had_as_general_use: Optional[Union[List[E55Type], E55Type]] = None
    p130_shows_features_of: Optional[Union[List[E70Thing], E70Thing]] = None
    p130i_features_are_also_found_on: Optional[Union[List[E70Thing], E70Thing]] = None
    p16i_was_used_for: Optional[Union[List[E7Activity], E7Activity]] = None
    p43_has_dimension: Optional[Union[List[E54Dimension], E54Dimension]] = None


class E93Presence(E92SpacetimeVolume):
    p164_is_temporally_specified_by: Optional[
        Union[List[E52TimeSpan], E52TimeSpan]
    ] = None
    p166_was_a_presence_of: Optional[
        Union[List[E92SpacetimeVolume], E92SpacetimeVolume]
    ] = None
    p167_was_within: Optional[Union[List[E53Place], E53Place]] = None
    p195_was_a_presence_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p197_covered_parts_of: Optional[Union[List[E53Place], E53Place]] = None


class E5Event(E4Period):
    p11_had_participant: Optional[Union[List[E39Actor], E39Actor]] = None
    p12_occurred_in_the_presence_of: Optional[
        Union[List[E77PersistentItem], E77PersistentItem]
    ] = None
    p20i_was_purpose_of: Optional[Union[List[E7Activity], E7Activity]] = None


class E72LegalObject(E70Thing):
    p104_is_subject_to: Optional[Union[List[E30Right], E30Right]] = None
    p105_right_held_by: Optional[Union[List[E39Actor], E39Actor]] = None


class E18PhysicalThing(E72LegalObject):
    p111i_was_added_by: Optional[Union[List[E79PartAddition], E79PartAddition]] = None
    p113i_was_removed_by: Optional[Union[List[E80PartRemoval], E80PartRemoval]] = None
    p123i_resulted_from: Optional[
        Union[List[E81Transformation], E81Transformation]
    ] = None
    p124i_was_transformed_by: Optional[
        Union[List[E81Transformation], E81Transformation]
    ] = None
    p128_carries: Optional[Union[List[E90SymbolicObject], E90SymbolicObject]] = None
    p13i_was_destroyed_by: Optional[Union[List[E6Destruction], E6Destruction]] = None
    p156_occupies: Optional[Union[List[E53Place], E53Place]] = None
    p157i_provides_reference_space_for: Optional[Union[List[E53Place], E53Place]] = None
    p195i_had_presence: Optional[Union[List[E93Presence], E93Presence]] = None
    p196_defines: Optional[Union[List[E92SpacetimeVolume], E92SpacetimeVolume]] = None
    p198_holds_or_supports: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p198i_is_held_or_supported_by: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p24i_changed_ownership_through: Optional[
        Union[List[E8Acquisition], E8Acquisition]
    ] = None
    p30i_custody_transferred_through: Optional[
        Union[List[E10TransferofCustody], E10TransferofCustody]
    ] = None
    p31i_was_modified_by: Optional[Union[List[E11Modification], E11Modification]] = None
    p34i_was_assessed_by: Optional[
        Union[List[E14ConditionAssessment], E14ConditionAssessment]
    ] = None
    p39i_was_measured_by: Optional[Union[List[E16Measurement], E16Measurement]] = None
    p44_has_condition: Optional[Union[List[E3ConditionState], E3ConditionState]] = None
    p45_consists_of: Optional[Union[List[E57Material], E57Material]] = None
    p46_is_composed_of: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None
    p46i_forms_part_of: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None
    p49_has_former_or_current_keeper: Optional[Union[List[E39Actor], E39Actor]] = None
    p50_has_current_keeper: Optional[Union[List[E39Actor], E39Actor]] = None
    p51_has_former_or_current_owner: Optional[Union[List[E39Actor], E39Actor]] = None
    p52_has_current_owner: Optional[Union[List[E39Actor], E39Actor]] = None
    p53_has_former_or_current_location: Optional[Union[List[E53Place], E53Place]] = None
    p59_has_section: Optional[Union[List[E53Place], E53Place]] = None
    p8i_witnessed: Optional[Union[List[E4Period], E4Period]] = None


class E19PhysicalObject(E18PhysicalThing):
    p188i_is_production_tool_for: Optional[
        Union[List[E99ProductType], E99ProductType]
    ] = None
    p25i_moved_by: Optional[Union[List[E9Move], E9Move]] = None
    p54_has_current_permanent_location: Optional[Union[List[E53Place], E53Place]] = None
    p55_has_current_location: Optional[Union[List[E53Place], E53Place]] = None
    p56_bears_feature: Optional[
        Union[List[E26PhysicalFeature], E26PhysicalFeature]
    ] = None
    p57_has_number_of_parts: Optional[Union[List[str], str]] = None


class E20BiologicalObject(E19PhysicalObject):
    pass


class E21Person(E20BiologicalObject, E39Actor):
    p100i_died_in: Optional[Union[List[E69Death], E69Death]] = None
    p152_has_parent: Optional[Union[List[E21Person], E21Person]] = None
    p152i_is_parent_of: Optional[Union[List[E21Person], E21Person]] = None
    p96i_gave_birth: Optional[Union[List[E67Birth], E67Birth]] = None
    p97i_was_father_for: Optional[Union[List[E67Birth], E67Birth]] = None
    p98i_was_born: Optional[Union[List[E67Birth], E67Birth]] = None


class E74Group(E39Actor):
    p107_has_current_or_former_member: Optional[Union[List[E39Actor], E39Actor]] = None
    p144i_gained_member_by: Optional[Union[List[E85Joining], E85Joining]] = None
    p146i_lost_member_by: Optional[Union[List[E86Leaving], E86Leaving]] = None
    p151i_participated_in: Optional[Union[List[E66Formation], E66Formation]] = None
    p95i_was_formed_by: Optional[Union[List[E66Formation], E66Formation]] = None
    p99i_was_dissolved_by: Optional[Union[List[E68Dissolution], E68Dissolution]] = None


class E71HumanMadeThing(E70Thing):
    p102_has_title: Optional[Union[List[E35Title], E35Title]] = None
    p103_was_intended_for: Optional[Union[List[E55Type], E55Type]] = None
    p19i_was_made_for: Optional[Union[List[E7Activity], E7Activity]] = None


class E63BeginningofExistence(E5Event):
    p92_brought_into_existence: Optional[
        Union[List[E77PersistentItem], E77PersistentItem]
    ] = None


class E64EndofExistence(E5Event):
    p93_took_out_of_existence: Optional[
        Union[List[E77PersistentItem], E77PersistentItem]
    ] = None


class E7Activity(E5Event):
    p125_used_object_of_type: Optional[Union[List[E55Type], E55Type]] = None
    p134_continued: Optional[Union[List[E7Activity], E7Activity]] = None
    p134i_was_continued_by: Optional[Union[List[E7Activity], E7Activity]] = None
    p14_carried_out_by: Optional[Union[List[E39Actor], E39Actor]] = None
    p15_was_influenced_by: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p16_used_specific_object: Optional[Union[List[E70Thing], E70Thing]] = None
    p17_was_motivated_by: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p19_was_intended_use_of: Optional[
        Union[List[E71HumanMadeThing], E71HumanMadeThing]
    ] = None
    p20_had_specific_purpose: Optional[Union[List[E5Event], E5Event]] = None
    p21_had_general_purpose: Optional[Union[List[E55Type], E55Type]] = None
    p32_used_general_technique: Optional[Union[List[E55Type], E55Type]] = None
    p33_used_specific_technique: Optional[
        Union[List[E29DesignorProcedure], E29DesignorProcedure]
    ] = None


class E24PhysicalHumanMadeThing(E71HumanMadeThing, E18PhysicalThing):
    p108i_was_produced_by: Optional[Union[List[E12Production], E12Production]] = None
    p110i_was_augmented_by: Optional[
        Union[List[E79PartAddition], E79PartAddition]
    ] = None
    p112i_was_diminished_by: Optional[
        Union[List[E80PartRemoval], E80PartRemoval]
    ] = None
    p62_depicts: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p65_shows_visual_item: Optional[Union[List[E36VisualItem], E36VisualItem]] = None


class E28ConceptualObject(E71HumanMadeThing):
    p94i_was_created_by: Optional[Union[List[E65Creation], E65Creation]] = None


class E90SymbolicObject(E72LegalObject, E28ConceptualObject):
    p106_is_composed_of: Optional[
        Union[List[E90SymbolicObject], E90SymbolicObject]
    ] = None
    p106i_forms_part_of: Optional[
        Union[List[E90SymbolicObject], E90SymbolicObject]
    ] = None
    p128i_is_carried_by: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p142i_was_used_in: Optional[
        Union[List[E15IdentifierAssignment], E15IdentifierAssignment]
    ] = None
    p165i_is_incorporated_in: Optional[
        Union[List[E73InformationObject], E73InformationObject]
    ] = None
    p190_has_symbolic_content: Optional[Union[List[str], str]] = None


class E11Modification(E7Activity):
    p126_employed: Optional[Union[List[E57Material], E57Material]] = None
    p31_has_modified: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None


class E12Production(E63BeginningofExistence, E11Modification):
    p108_has_produced: Optional[
        Union[List[E24PhysicalHumanMadeThing], E24PhysicalHumanMadeThing]
    ] = None
    p186_produced_thing_of_product_type: Optional[
        Union[List[E99ProductType], E99ProductType]
    ] = None


class E65Creation(E63BeginningofExistence, E7Activity):
    p94_has_created: Optional[
        Union[List[E28ConceptualObject], E28ConceptualObject]
    ] = None


class E66Formation(E63BeginningofExistence, E7Activity):
    p151_was_formed_from: Optional[Union[List[E74Group], E74Group]] = None
    p95_has_formed: Optional[Union[List[E74Group], E74Group]] = None


class E67Birth(E63BeginningofExistence):
    p96_by_mother: Optional[Union[List[E21Person], E21Person]] = None
    p97_from_father: Optional[Union[List[E21Person], E21Person]] = None
    p98_brought_into_life: Optional[Union[List[E21Person], E21Person]] = None


class E81Transformation(E64EndofExistence, E63BeginningofExistence):
    p123_resulted_in: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None
    p124_transformed: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None


class E68Dissolution(E64EndofExistence):
    p99_dissolved: Optional[Union[List[E74Group], E74Group]] = None


class E69Death(E64EndofExistence):
    p100_was_death_of: Optional[Union[List[E21Person], E21Person]] = None


class E6Destruction(E64EndofExistence):
    p13_destroyed: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None


class E10TransferofCustody(E7Activity):
    p28_custody_surrendered_by: Optional[Union[List[E39Actor], E39Actor]] = None
    p29_custody_received_by: Optional[Union[List[E39Actor], E39Actor]] = None
    p30_transferred_custody_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None


class E13AttributeAssignment(E7Activity):
    p140_assigned_attribute_to: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p141_assigned: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p177_assigned_property_of_type: Optional[Union[List[E55Type], E55Type]] = None


class E85Joining(E7Activity):
    p143_joined: Optional[Union[List[E39Actor], E39Actor]] = None
    p144_joined_with: Optional[Union[List[E74Group], E74Group]] = None


class E86Leaving(E7Activity):
    p145_separated: Optional[Union[List[E39Actor], E39Actor]] = None
    p146_separated_from: Optional[Union[List[E74Group], E74Group]] = None


class E87CurationActivity(E7Activity):
    p147_curated: Optional[Union[List[E78CuratedHolding], E78CuratedHolding]] = None


class E8Acquisition(E7Activity):
    p22_transferred_title_to: Optional[Union[List[E39Actor], E39Actor]] = None
    p23_transferred_title_from: Optional[Union[List[E39Actor], E39Actor]] = None
    p24_transferred_title_of: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None


class E9Move(E7Activity):
    p25_moved: Optional[Union[List[E19PhysicalObject], E19PhysicalObject]] = None
    p26_moved_to: Optional[Union[List[E53Place], E53Place]] = None
    p27_moved_from: Optional[Union[List[E53Place], E53Place]] = None


class E22HumanMadeObject(E19PhysicalObject, E24PhysicalHumanMadeThing):
    pass


class E26PhysicalFeature(E18PhysicalThing):
    p56i_is_found_on: Optional[Union[List[E19PhysicalObject], E19PhysicalObject]] = None


class E25HumanMadeFeature(E26PhysicalFeature, E24PhysicalHumanMadeThing):
    pass


class E78CuratedHolding(E24PhysicalHumanMadeThing):
    p109_has_current_or_former_curator: Optional[Union[List[E39Actor], E39Actor]] = None
    p147i_was_curated_by: Optional[
        Union[List[E87CurationActivity], E87CurationActivity]
    ] = None


class E55Type(E28ConceptualObject):
    p101i_was_use_of: Optional[Union[List[E70Thing], E70Thing]] = None
    p103i_was_intention_of: Optional[
        Union[List[E71HumanMadeThing], E71HumanMadeThing]
    ] = None
    p125i_was_type_of_object_used_in: Optional[
        Union[List[E7Activity], E7Activity]
    ] = None
    p127_has_broader_term: Optional[Union[List[E55Type], E55Type]] = None
    p127i_has_narrower_term: Optional[Union[List[E55Type], E55Type]] = None
    p135i_was_created_by: Optional[Union[List[E83TypeCreation], E83TypeCreation]] = None
    p137i_is_exemplified_by: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p150_defines_typical_parts_of: Optional[Union[List[E55Type], E55Type]] = None
    p150i_defines_typical_wholes_for: Optional[Union[List[E55Type], E55Type]] = None
    p177i_is_type_of_property_assigned: Optional[
        Union[List[E13AttributeAssignment], E13AttributeAssignment]
    ] = None
    p21i_was_purpose_of: Optional[Union[List[E7Activity], E7Activity]] = None
    p2i_is_type_of: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p32i_was_technique_of: Optional[Union[List[E7Activity], E7Activity]] = None
    p42i_was_assigned_by: Optional[
        Union[List[E17TypeAssignment], E17TypeAssignment]
    ] = None


class E89PropositionalObject(E28ConceptualObject):
    p129_is_about: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p148_has_component: Optional[
        Union[List[E89PropositionalObject], E89PropositionalObject]
    ] = None
    p148i_is_component_of: Optional[
        Union[List[E89PropositionalObject], E89PropositionalObject]
    ] = None
    p67_refers_to: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None


class E73InformationObject(E89PropositionalObject, E90SymbolicObject):
    p165_incorporates: Optional[
        Union[List[E90SymbolicObject], E90SymbolicObject]
    ] = None


class E41Appellation(E90SymbolicObject):
    p139_has_alternative_form: Optional[
        Union[List[E41Appellation], E41Appellation]
    ] = None
    p1i_identifies: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p76i_provides_access_to: Optional[Union[List[E39Actor], E39Actor]] = None


class E83TypeCreation(E65Creation):
    p135_created_type: Optional[Union[List[E55Type], E55Type]] = None
    p136_was_based_on: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None


class E79PartAddition(E11Modification):
    p110_augmented: Optional[
        Union[List[E24PhysicalHumanMadeThing], E24PhysicalHumanMadeThing]
    ] = None
    p111_added: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None


class E80PartRemoval(E11Modification):
    p112_diminished: Optional[
        Union[List[E24PhysicalHumanMadeThing], E24PhysicalHumanMadeThing]
    ] = None
    p113_removed: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None


class E14ConditionAssessment(E13AttributeAssignment):
    p34_concerned: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None
    p35_has_identified: Optional[Union[List[E3ConditionState], E3ConditionState]] = None


class E15IdentifierAssignment(E13AttributeAssignment):
    p142_used_constituent: Optional[
        Union[List[E90SymbolicObject], E90SymbolicObject]
    ] = None
    p37_assigned: Optional[Union[List[E42Identifier], E42Identifier]] = None
    p38_deassigned: Optional[Union[List[E42Identifier], E42Identifier]] = None


class E16Measurement(E13AttributeAssignment):
    p39_measured: Optional[Union[List[E18PhysicalThing], E18PhysicalThing]] = None
    p40_observed_dimension: Optional[Union[List[E54Dimension], E54Dimension]] = None


class E17TypeAssignment(E13AttributeAssignment):
    p41_classified: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p42_assigned: Optional[Union[List[E55Type], E55Type]] = None


class E96Purchase(E8Acquisition):
    p179_had_sales_price: Optional[
        Union[List[E97MonetaryAmount], E97MonetaryAmount]
    ] = None


class E56Language(E55Type):
    p72i_is_language_of: Optional[
        Union[List[E33LinguisticObject], E33LinguisticObject]
    ] = None


class E57Material(E55Type):
    p126i_was_employed_in: Optional[
        Union[List[E11Modification], E11Modification]
    ] = None
    p45i_is_incorporated_in: Optional[
        Union[List[E18PhysicalThing], E18PhysicalThing]
    ] = None
    p68i_use_foreseen_by: Optional[
        Union[List[E29DesignorProcedure], E29DesignorProcedure]
    ] = None


class E58MeasurementUnit(E55Type):
    p91i_is_unit_of: Optional[Union[List[E54Dimension], E54Dimension]] = None


class E99ProductType(E55Type):
    p186i_is_produced_by: Optional[Union[List[E12Production], E12Production]] = None
    p187_has_production_plan: Optional[
        Union[List[E29DesignorProcedure], E29DesignorProcedure]
    ] = None
    p188_requires_production_tool: Optional[
        Union[List[E19PhysicalObject], E19PhysicalObject]
    ] = None


class E30Right(E89PropositionalObject):
    p104i_applies_to: Optional[Union[List[E72LegalObject], E72LegalObject]] = None
    p75i_is_possessed_by: Optional[Union[List[E39Actor], E39Actor]] = None


class E29DesignorProcedure(E73InformationObject):
    p187i_is_production_plan_for: Optional[
        Union[List[E99ProductType], E99ProductType]
    ] = None
    p33i_was_used_by: Optional[Union[List[E7Activity], E7Activity]] = None
    p68_foresees_use_of: Optional[Union[List[E57Material], E57Material]] = None
    p69_has_association_with: Optional[
        Union[List[E29DesignorProcedure], E29DesignorProcedure]
    ] = None
    p69i_is_associated_with: Optional[
        Union[List[E29DesignorProcedure], E29DesignorProcedure]
    ] = None


class E31Document(E73InformationObject):
    p70_documents: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None


class E33LinguisticObject(E73InformationObject):
    p72_has_language: Optional[Union[List[E56Language], E56Language]] = None
    p73_has_translation: Optional[
        Union[List[E33LinguisticObject], E33LinguisticObject]
    ] = None
    p73i_is_translation_of: Optional[
        Union[List[E33LinguisticObject], E33LinguisticObject]
    ] = None


class E36VisualItem(E73InformationObject):
    p138_represents: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None
    p65i_is_shown_by: Optional[
        Union[List[E24PhysicalHumanMadeThing], E24PhysicalHumanMadeThing]
    ] = None


class E33E41LinguisticAppellation(E41Appellation, E33LinguisticObject):
    pass


class E35Title(E33LinguisticObject, E41Appellation):
    p102i_is_title_of: Optional[
        Union[List[E71HumanMadeThing], E71HumanMadeThing]
    ] = None


class E42Identifier(E41Appellation):
    p37i_was_assigned_by: Optional[
        Union[List[E15IdentifierAssignment], E15IdentifierAssignment]
    ] = None
    p38i_was_deassigned_by: Optional[
        Union[List[E15IdentifierAssignment], E15IdentifierAssignment]
    ] = None
    p48i_is_preferred_identifier_of: Optional[
        Union[List[E1CRMEntity], E1CRMEntity]
    ] = None


class E27Site(E26PhysicalFeature):
    pass


class E98Currency(E58MeasurementUnit):
    p180i_was_currency_of: Optional[
        Union[List[E97MonetaryAmount], E97MonetaryAmount]
    ] = None


class E32AuthorityDocument(E31Document):
    p71_lists: Optional[Union[List[E1CRMEntity], E1CRMEntity]] = None


class E37Mark(E36VisualItem):
    pass


class E34Inscription(E33LinguisticObject, E37Mark):
    pass


E1CRMEntity.update_forward_refs()
E2TemporalEntity.update_forward_refs()
E52TimeSpan.update_forward_refs()
E53Place.update_forward_refs()
E54Dimension.update_forward_refs()
E77PersistentItem.update_forward_refs()
E92SpacetimeVolume.update_forward_refs()
PC102hastitle.update_forward_refs()
PC107hascurrentorformermember.update_forward_refs()
PC130showsfeaturesof.update_forward_refs()
PC136wasbasedon.update_forward_refs()
PC137exemplifies.update_forward_refs()
PC138represents.update_forward_refs()
PC139hasalternativeform.update_forward_refs()
PC144joinedwith.update_forward_refs()
PC14carriedoutby.update_forward_refs()
PC16usedspecificobject.update_forward_refs()
PC189approximates.update_forward_refs()
PC19wasintendeduseof.update_forward_refs()
PC3hasnote.update_forward_refs()
PC62depicts.update_forward_refs()
PC67refersto.update_forward_refs()
PC69hasassociationwith.update_forward_refs()
E3ConditionState.update_forward_refs()
E4Period.update_forward_refs()
E97MonetaryAmount.update_forward_refs()
E39Actor.update_forward_refs()
E70Thing.update_forward_refs()
E93Presence.update_forward_refs()
E5Event.update_forward_refs()
E21Person.update_forward_refs()
E74Group.update_forward_refs()
E71HumanMadeThing.update_forward_refs()
E72LegalObject.update_forward_refs()
E63BeginningofExistence.update_forward_refs()
E64EndofExistence.update_forward_refs()
E7Activity.update_forward_refs()
E24PhysicalHumanMadeThing.update_forward_refs()
E28ConceptualObject.update_forward_refs()
E90SymbolicObject.update_forward_refs()
E18PhysicalThing.update_forward_refs()
E12Production.update_forward_refs()
E65Creation.update_forward_refs()
E66Formation.update_forward_refs()
E67Birth.update_forward_refs()
E81Transformation.update_forward_refs()
E68Dissolution.update_forward_refs()
E69Death.update_forward_refs()
E6Destruction.update_forward_refs()
E10TransferofCustody.update_forward_refs()
E11Modification.update_forward_refs()
E13AttributeAssignment.update_forward_refs()
E85Joining.update_forward_refs()
E86Leaving.update_forward_refs()
E87CurationActivity.update_forward_refs()
E8Acquisition.update_forward_refs()
E9Move.update_forward_refs()
E22HumanMadeObject.update_forward_refs()
E25HumanMadeFeature.update_forward_refs()
E78CuratedHolding.update_forward_refs()
E55Type.update_forward_refs()
E89PropositionalObject.update_forward_refs()
E73InformationObject.update_forward_refs()
E41Appellation.update_forward_refs()
E19PhysicalObject.update_forward_refs()
E26PhysicalFeature.update_forward_refs()
E83TypeCreation.update_forward_refs()
E79PartAddition.update_forward_refs()
E80PartRemoval.update_forward_refs()
E14ConditionAssessment.update_forward_refs()
E15IdentifierAssignment.update_forward_refs()
E16Measurement.update_forward_refs()
E17TypeAssignment.update_forward_refs()
E96Purchase.update_forward_refs()
E56Language.update_forward_refs()
E57Material.update_forward_refs()
E58MeasurementUnit.update_forward_refs()
E99ProductType.update_forward_refs()
E30Right.update_forward_refs()
E29DesignorProcedure.update_forward_refs()
E31Document.update_forward_refs()
E33LinguisticObject.update_forward_refs()
E36VisualItem.update_forward_refs()
E33E41LinguisticAppellation.update_forward_refs()
E35Title.update_forward_refs()
E42Identifier.update_forward_refs()
E20BiologicalObject.update_forward_refs()
E27Site.update_forward_refs()
E98Currency.update_forward_refs()
E32AuthorityDocument.update_forward_refs()
E34Inscription.update_forward_refs()
E37Mark.update_forward_refs()
