from django.db import models
from django.utils import  timezone
# Create your models here.
now = timezone.now

ESTATUS = (
    ('OK', 'OK'),
    ('RIESGO', 'RIESGO'),
    ('INCIDENCIA', 'INCIDENCIA'),
)


class EstatusInterATT(models.Model):
    macno_centro_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                            verbose_name="MACNO CENTRO  BUNDLE-ETHER 300",
                                                            blank=True, null=True, default='OK')
    
    macno_centro_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                                verbose_name="MACNO CENTRO  BUNDLE-ETHER 300",
                                                                blank=True, null=True)

    msomex01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOMEX01 VLAN´S",
                                            blank=True, null=True, default='OK')
    
    msomex01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOMEX01 VLAN´S", blank=True,
                                                 null=True)

    msomex02_bundle_ether_500_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOMEX02 BUNDLE-ETHER 500", blank=True,
                                                           null=True, default='OK')

    msomex02_bundle_ether_500_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOMEX02 BUNDLE-ETHER 500",
                                                             blank=True, null=True)

    msomex02_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOMEX02 VLAN´S",
                                             blank=True, null=True, default='OK')
    msomex02_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOMEX02 VLAN´S", blank=True,
                                                 null=True)

    msomex03_bundle_ether_500_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOMEX03 BUNDLE-ETHER 500", blank=True,
                                                           null=True, default='OK')

    msomex03_bundle_ether_500_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOMEX03 BUNDLE-ETHER 500",
                                                             blank=True, null=True)

    msomex03_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOMEX03 VLAN´S",
                                             blank=True, null=True, default='OK')

    msomex03_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOMEX03 VLAN´S", blank=True,
                                                 null=True)

    msomex04_bundle_ether_400_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOMEX04 BUNDLE-ETHER 400", blank=True,
                                                           null=True, default='OK')

    msomex04_bundle_ether_400_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOMEX04 BUNDLE-ETHER 400",
                                                             blank=True, null=True)

    msomex04_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOMEX04 VLAN´S",
                                             blank=True, null=True, default='OK')

    msomex04_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOMEX04 VLAN´S", blank=True,
                                                 null=True)

    mexzum8148_bundle_ether_500_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                             verbose_name="MEXZUM8148 BUNDLE-ETHER 500",
                                                             blank=True, null=True, default='OK')

    mexzum8148_bundle_ether_500_comentarios = models.CharField(max_length=200,
                                                               verbose_name="MEXZUM8148 BUNDLE-ETHER 500",
                                                               blank=True, null=True)

    mexzum8148_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MEXZUM8148 VLAN´S",
                                               blank=True, null=True, default='OK')

    mexzum8148_vlan_comentarios = models.CharField(max_length=200, verbose_name="MEXZUM8148 VLAN´S",
                                                   blank=True, null=True)

    msomty01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOGDL01 BUNDLE-ETHER 300", blank=True,
                                                           null=True, default='OK')

    msomty01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOMTY01 BUNDLE-ETHER 300",
                                                             blank=True, null=True)

    msomty01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOMTY01 VLAN´S",
                                             blank=True, null=True, default='OK')
                                             
    msomty01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOMTY01 VLAN´S", blank=True,
                                                 null=True)

    hmty0237_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="HMTY0237 VLAN´S",
                                             blank=True, null=True, default='OK')
    
    hmty0237_vlan_comentarios = models.CharField(max_length=200, verbose_name="HMTY0237 VLAN´S", blank=True,
                                                 null=True)

    msogdl01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOGDL01 BUNDLE-ETHER 300", blank=True,
                                                           null=True, default='OK')

    msogdl01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOGDL01 BUNDLE-ETHER 300",
                                                             blank=True, null=True)

    msogdl01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOGDL01 VLAN´S",
                                             blank=True, null=True, default='OK')

    msogdl01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOGDL01 VLAN´S", blank=True,
                                                 null=True)

    msotjp01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOTJP01 BUNDLE-ETHE", blank=True,
                                                           null=True, default='OK')
    
    msotjp01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOTJP01 BUNDLE-ETHER 300",
                                                             blank=True, null=True)

    msotjp01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOTJP01 VLAN´S",
                                             blank=True, null=True, default='OK')
    
    msotjp01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOTJP01 VLAN´S", blank=True,
                                                 null=True)

    msocjup01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                            verbose_name="MSOCJUP01 BUNDLE-ETHER 300",
                                                            blank=True, null=True, default='OK')
    
    msocjup01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                              verbose_name="MSOCJUP01 BUNDLE-ETHER 300",
                                                              blank=True, null=True)

    msocjup01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOCJUP01 VLAN´S",
                                              blank=True, null=True, default='OK')
    
    msocjup01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOCJUP01 VLAN´S", blank=True,
                                                  null=True)

    msopue01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                            verbose_name="MSOPUE01  BUNDLE-ETHER 300",
                                                            blank=True, null=True, default='OK')
    
    msopue01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOPUE01  BUNDLE-ETHER 300",
                                                             blank=True, null=True)

    msopue01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOPUE01  VLAN´S",
                                              blank=True, null=True, default='OK')
    
    msopue01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOPUE01  VLAN´S", blank=True,
                                                 null=True)

    rsopue01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="RSOPUE01  VLAN´S",
                                              blank=True, null=True, default='OK')
    
    rsopue01_vlan_comentarios = models.CharField(max_length=200, verbose_name="RSOPUE01  VLAN´S", blank=True,
                                                 null=True)

    tam_htpc0030_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                               verbose_name="TAM_HTPC0030 BUNDLE-ETHER 300",
                                                               blank=True, null=True, default='OK')

    tam_htpc0030_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                                 verbose_name="TAM_HTPC0030 BUNDLE-ETHER 300",
                                                                 blank=True, null=True)

    tam_htpc0030_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                  verbose_name="TAM_HTPC0030  VLAN´S", blank=True, null=True,
                                                  default='OK')

    tam_htpc0030_vlan_comentarios = models.CharField(max_length=200, verbose_name="TAM_HTPC0030  VLAN´S",
                                                     blank=True, null=True)

    tam_rsotpoc01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                                verbose_name="TAM_RSOTPOC01 BUNDLE-ETHER 300",
                                                                blank=True, null=True, default='OK')

    tam_rsotpoc01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                                  verbose_name="TAM_RSOTPOC01 BUNDLE-ETHER 300",
                                                                  blank=True, null=True)

    tam_rsotpoc01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                  verbose_name="TAM_RSOTPOC01 VLAN´S", blank=True, null=True,
                                                  default='OK')

    tam_rsotpoc01_vlan_comentarios = models.CharField(max_length=200, verbose_name="TAM_RSOTPOC01 VLAN´S",
                                                      blank=True, null=True)

    nld_rsonld01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                               verbose_name="NLD_RSONLD01 BUNDLE-ETHER 300",
                                                               blank=True, null=True, default='OK')

    nld_rsonld01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                                 verbose_name="NLD_RSONLD01 BUNDLE-ETHER 300",
                                                                 blank=True, null=True)

    nld_rsonld01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                 verbose_name="NLD_RSONLD01 VLAN´S", blank=True, null=True,
                                                 default='OK')
    nld_rsonld01_vlan_comentarios = models.CharField(max_length=200, verbose_name="NLD_RSONLD01 VLAN´S",
                                                     blank=True, null=True)



    tor_250_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                   verbose_name="TOR-250 BUNDLE-ETHER 300", blank=True,
                                                   null=True, default='OK')
    tor_250_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                            verbose_name="TOR-250 BUNDLE-ETHER 300",
                                                            blank=True, null=True)




    tor_250_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="TOR-250 VLAN´S", blank=True,
                                     null=True, default='OK')
    tor_250_vlan_comentarios = models.CharField(max_length=200, verbose_name="TOR-250 VLAN´S", blank=True,
                                                null=True)






    rey_rsorey01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                               verbose_name="REY_RSOREY01 BUNDLE-ETHER 300",
                                                               blank=True, null=True, default='OK')
    rey_rsorey01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                                 verbose_name="REY_RSOREY01 BUNDLE-ETHER 300",
                                                                 blank=True, null=True)






    rey_rsorey01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                 verbose_name="REY_RSOREY01 VLAN´S", blank=True, null=True,
                                                 default='OK')
    rey_rsorey01_vlan_comentarios = models.CharField(max_length=200, verbose_name="REY_RSOREY01 VLAN´S",
                                                     blank=True, null=True)





    rsochi01_bundle_ether_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="RSOCHI01 BUNDLE-ETHER 300", blank=True,
                                                           null=True, default='OK')
    rsochi01_bundle_ether_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="RSOCHI01 BUNDLE-ETHER 300",
                                                             blank=True, null=True)





    rsochi01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="RSOCHI01 VLAN´S",
                                             blank=True, null=True, default='OK')
    rsochi01_vlan_comentarios = models.CharField(max_length=200, verbose_name="RSOCHI01 VLAN´S", blank=True,
                                                 null=True)



    msocab01_port_channel_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="MSOCAB01 PORT-CHANNEL 300", blank=True,
                                                           null=True, default='OK')
    msocab01_port_channel_300_comentarios = models.CharField(max_length=200,
                                                             verbose_name="MSOCAB01 PORT-CHANNEL 300",
                                                             blank=True, null=True)





    msocab01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOCAB01 VLAN´S",
                                             blank=True, null=True, default='OK')
    msocab01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOCAB01 VLAN´S", blank=True,
                                                 null=True)





    rsotol01_ether_trunk_100_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                          verbose_name="RSOTOL01 ETHER-TRUNK 100", blank=True,
                                                          null=True, default='OK')
    rsotol01_ether_trunk_100_comentarios = models.CharField(max_length=200,
                                                            verbose_name="RSOTOL01 ETHER-TRUNK 100",
                                                            blank=True, null=True)



    rsotol01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="RSOTOL01 VLAN´S",
                                             blank=True, null=True, default='OK')
    rsotol01_vlan_comentarios = models.CharField(max_length=200, verbose_name="RSOTOL01 VLAN´S", blank=True,
                                                 null=True)





    msotol01_ether_trunk_100_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                          verbose_name="MSOTOL01 ETHER-TRUNK 100", blank=True,
                                                          null=True, default='OK')
    msotol01_ether_trunk_100_comentarios = models.CharField(max_length=200,
                                                            verbose_name="MSOTOL01 ETHER-TRUNK 100",
                                                            blank=True, null=True)





    msotol01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MSOTOL01 VLAN´S",
                                             blank=True, null=True, default='OK')
    msotol01_vlan_comentarios = models.CharField(max_length=200, verbose_name="MSOTOL01 VLAN´S", blank=True,
                                                 null=True)




    can_rsocun01_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="CAN_RSOCUN01-TRUNK", blank=True, null=True,
                                                    default='OK')
    can_rsocun01_trunk_comentarios = models.CharField(max_length=200, verbose_name="CAN_RSOCUN01-TRUNK",
                                                      blank=True, null=True)




    can_rsocun01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                   verbose_name="CAN_RSOCUN01-VLAN´S", blank=True, null=True,
                                                   default='OK')
    can_rsocun01_vlan_comentarios = models.CharField(max_length=200, verbose_name="CAN_RSOCUN01-VLAN´S",
                                                     blank=True, null=True)





    mer_msomer01_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="MER_MSOMER01-TRUNK", blank=True, null=True,
                                                    default='OK')
    mer_msomer01_trunk_comentarios = models.CharField(max_length=200, verbose_name="MER_MSOMER01-TRUNK",
                                                      blank=True, null=True)





    mer_msomer02_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="MER_MSOMER02-TRUNK", blank=True, null=True,
                                                    default='OK')
    mer_msomer02_trunk_comentarios = models.CharField(max_length=200, verbose_name="MER_MSOMER02-TRUNK",
                                                      blank=True, null=True)





    mer_msomer02_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                   verbose_name="MER_MSOMER02-VLAN´S", blank=True, null=True,
                                                   default='OK')
    mer_msomer02_vlan_comentarios = models.CharField(max_length=200, verbose_name="MER_MSOMER02-VLAN´S",
                                                     blank=True, null=True)





    tap_chptap0102_port_channel_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                                  verbose_name="TAP_CHPTAP0102  PORT-CHANNEL 300",
                                                                  blank=True, null=True, default='OK')
    tap_chptap0102_port_channel_300_comentarios = models.CharField(max_length=200,
                                                                   verbose_name="TAP_CHPTAP0102  PORT-CHANNEL 300",
                                                                   blank=True, null=True)





    tep_chptap0102_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="TEP_CHPTAP0102-VLAN´S", blank=True, null=True,
                                                     default='OK')
    tep_chptap0102_vlan_comentarios = models.CharField(max_length=200, verbose_name="TEP_CHPTAP0102-VLAN´S",
                                                       blank=True, null=True)



    uru_micuru1210_port_channel_300_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                                  verbose_name="URU_MICURU1210  PORT-CHANNEL 300",
                                                                  blank=True, null=True, default='OK')
    uru_micuru1210_port_channel_300_comentarios = models.CharField(max_length=200,
                                                                   verbose_name="URU_MICURU1210  PORT-CHANNEL 300",
                                                                   blank=True, null=True)




    uru_micuru1210_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="URU_MICURU1210-VLAN´S", blank=True, null=True,
                                                     default='OK')
    uru_micuru1210_vlan_comentarios = models.CharField(max_length=200, verbose_name="URU_MICURU1210-VLAN´S",
                                                       blank=True, null=True)




    vhe_msovhe01_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="VHE_MSOVHE01-TRUNK", blank=True, null=True,
                                                    default='OK')
    vhe_msovhe01_trunk_comentarios = models.CharField(max_length=200, verbose_name="VHE_MSOVHE01-TRUNK",
                                                      blank=True, null=True)



    vhe_msovhe01_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                   verbose_name="VHE_MSOVHE01-VLAN´S  ", blank=True, null=True,
                                                   default='OK')
    vhe_msovhe01_vlan_comentarios = models.CharField(max_length=200, verbose_name="VHE_MSOVHE01-VLAN´S  ",
                                                     blank=True, null=True)



    uru_micsae1190_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                      verbose_name="URU_MICSAE1190-TRUNK", blank=True,
                                                      null=True, default='OK')
    uru_micsae1190_trunk_comentarios = models.CharField(max_length=200, verbose_name="URU_MICSAE1190-TRUNK",
                                                        blank=True, null=True)




    uru_micsae119_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="URU_MICSAE119-VLAN´S", blank=True, null=True,
                                                    default='OK')
    uru_micsae119_vlan_comentarios = models.CharField(max_length=200, verbose_name="URU_MICSAE119-VLAN´S",
                                                      blank=True, null=True)





    uru_micrys1186_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                      verbose_name="URU_MICRYS1186-TRUNK", blank=True,
                                                      null=True, default='OK')
    uru_micrys1186_trunk_comentarios = models.CharField(max_length=200, verbose_name="URU_MICRYS1186-TRUNK",
                                                        blank=True, null=True)




    uru_micrys1186_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="URU_MICRYS1186-VLAN´S  ", blank=True, null=True,
                                                     default='OK')
    uru_micrys1186_vlan_comentarios = models.CharField(max_length=200, verbose_name="URU_MICRYS1186-VLAN´S  ",
                                                       blank=True, null=True)




    mor_miczam1225_trunk_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                      verbose_name="MOR_MICZAM1225-TRUNK", blank=True,
                                                      null=True, default='OK')
    mor_miczam1225_trunk_comentarios = models.CharField(max_length=200, verbose_name="MOR_MICZAM1225-TRUNK",
                                                        blank=True, null=True)




    mor_miczam1225_vlan_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="MOR_MICZAM1225-VLAN´S  ", blank=True, null=True,
                                                     default='OK')

    mor_miczam1225_vlan_comentarios = models.CharField(max_length=200, verbose_name="MOR_MICZAM1225-VLAN´S  ",
                                                       blank=True, null=True)

    class Meta:
        verbose_name = "Interconfiguración ATT"
        verbose_name_plural = "Interconfiguración ATT"


class RutasInterEstatus(models.Model):
    puebla_cti_fuertes_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PUEBLA CTI FUERTES ",
                                                  blank=True, null=True, default='OK')
    tijuana_cti_pio_pico_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                    verbose_name="TIJUANA CTI PIO PICO ", blank=True, null=True,
                                                    default='OK')
    presa_cti_nextengo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PRESA CTI NEXTENGO ",
                                                  blank=True, null=True, default='OK')
    guadalajara_cti_tlaquepaque_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="GUADALAJARA CTI TLAQUEPAQUE", blank=True,
                                                           null=True, default='OK')
    monterrey_cti_mayo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MONTERREY CTI MAYO ",
                                                  blank=True, null=True, default='OK')
    monterrey_cti_revolucion_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                        verbose_name="MONTERREY CTI REVOLUCION ", blank=True, null=True,
                                                        default='OK')
    tlane_cti_vallejo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="TLANE CTI VALLEJO ",
                                                 blank=True, null=True, default='OK')

    presa_cti_nextengo_estatus_out = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PRESA CTI NEXTENGO OUT",
                                                  blank=True, null=True, default='OK')
    monterrey_cti_mayo_estatus_out = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MONTERREY CTI MAYO OUT",
                                                  blank=True, null=True, default='OK')
    tlane_cti_vallejo_estatus_out = models.CharField(choices=ESTATUS, max_length=45, verbose_name="TLANE CTI VALLEJO OUT",
                                                 blank=True, null=True, default='OK')
    tijuana_otay_estatus_out = models.CharField(choices=ESTATUS, max_length=45, verbose_name="TIJUANA OTAY OUT", blank=True,
                                            null=True, default='OK')
    monterrey_cti_revolucion_estatus_out = models.CharField(choices=ESTATUS, max_length=45,
                                                        verbose_name="MONTERREY CTI REVOLUCION OUT", blank=True, null=True,
                                                        default='OK')
    tlaquepaque_sbcq21pre_gdl_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                         verbose_name="TLAQUEPAQUE_SBCQ21PRE_GDL", blank=True,
                                                         null=True, default='OK')
    apodaca_sbcq21mty_mty_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="APODACA_SBCQ21MTY_MTY", blank=True, null=True,
                                                     default='OK')
    megacentro_sbcq21pre_cdmx_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                         verbose_name="MEGACENTRO_SBCQ21PRE_CDMX", blank=True,
                                                         null=True, default='OK')
    sbcq21mty_apodaca_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="SBCQ21MTY_APODACA",
                                                 blank=True, null=True, default='OK')
    sbg_ericcson_leo_tlaquepaque_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                            verbose_name="SBG_ERICCSON LEO_TLAQUEPAQUE", blank=True,
                                                            null=True, default='OK')
    sbg_ericcson_gdl_megacentro_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                           verbose_name="SBG_ERICCSON GDL_MEGACENTRO", blank=True,
                                                           null=True, default='OK')
    presa_sae_2884_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PRESA SAE-2884", blank=True, null=True,
                                default='OK')
    gdl_sae_2876_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="GDL SAE-2876", blank=True, null=True,
                                default='OK')
    mty_sae_2885_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MTY SAE-2885", blank=True, null=True,
                                default='OK')
    dfp_tcl_in_vallejo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="DFP_TCL_IN_VALLEJO",
                                                  blank=True, null=True, default='OK')
    dfn_tcl_in_nextengo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="DFN_TCL_IN_NEXTENGO",
                                                   blank=True, null=True, default='OK')
    mty_tcl_in_sanpedro_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MTY_TCL_IN_SANPEDRO",
                                                   blank=True, null=True, default='OK')
    mtp_tcl_in_revolucion_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                     verbose_name="MTP_TCL_IN_REVOLUCION", blank=True, null=True,
                                                     default='OK')
    gdl_tcl_in_bandera_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="GDL_TCL_IN_BANDERA",
                                                  blank=True, null=True, default='OK')
    gdl_tcl_in_tlaquepaque_estatus = models.CharField(choices=ESTATUS, max_length=45,
                                                      verbose_name="GDL_TCL_IN_TLAQUEPAQUE", blank=True, null=True,
                                                      default='OK')
    pue_tcl_in_fuertes_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PUE_TCL_IN_FUERTES",
                                                  blank=True, null=True, default='OK')
    pue_tcl_in_ctp_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="PUE_TCL_IN_CTP", blank=True,
                                              null=True, default='OK')
    gdl_sip_bandera_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="GDL SIP BANDERA",
                                               blank=True, null=True, default='OK')
    mty_sip_san_pedro_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MTY SIP SAN PEDRO",
                                                 blank=True, null=True, default='OK')
    tln_sip_nextengo_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="TLN SIP NEXTENGO",
                                                blank=True, null=True, default='OK')
    icx_marcatel_gdl_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="ICX_MARCATEL_GDL",
                                                blank=True, null=True, default='OK')
    mty_icx_vsbgmty_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="MTY_ICX_VSBGMTY",
                                               blank=True, null=True, default='OK')
    altan_vsbg2_mty_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="ALTAN_vSBG2_MTY",
                                               blank=True, null=True, default='OK')
    altan_vsbg2_tlane_estatus = models.CharField(choices=ESTATUS, max_length=45, verbose_name="ALTAN_vSBG2_TLANE",
                                                 blank=True, null=True, default='OK')

    class Meta:
        verbose_name = "Estatus Rutas de Interconexión"
        verbose_name_plural = "Health Check Estaus Rutas de Interconexión"


class RutasInterComentarios(models.Model):
    puebla_cti_fuertes_comentarios_IN = models.CharField(max_length=200, verbose_name=" IN PUEBLA CTI FUERTES ",
                                                         blank=True, null=True)
    tijuana_cti_pio_pico_comentarios_IN = models.CharField(max_length=200, verbose_name=" IN TIJUANA CTI PIO PICO ",
                                                           blank=True, null=True)
    presa_cti_nextengo_comentarios_IN = models.CharField(max_length=200, verbose_name=" IN PRESA CTI NEXTENGO ",
                                                         blank=True, null=True)
    guadalajara_cti_tlaquepaque_comentarios_IN = models.CharField(max_length=200,
                                                                  verbose_name=" IN GUADALAJARA CTI TLAQUEPAQUE",
                                                                  blank=True, null=True)
    monterrey_cti_mayo_comentarios_IN = models.CharField(max_length=200, verbose_name=" IN MONTERREY CTI MAYO ",
                                                         blank=True, null=True)
    monterrey_cti_revolucion_comentarios_IN = models.CharField(max_length=200,
                                                               verbose_name=" IN MONTERREY CTI REVOLUCION ", blank=True,
                                                               null=True)
    tlane_cti_vallejo_comentarios_IN = models.CharField(max_length=200, verbose_name=" IN TLANE CTI VALLEJO ",
                                                        blank=True, null=True)

    presa_cti_nextengo_comentarios = models.CharField(max_length=200, verbose_name="PRESA CTI NEXTENGO ", blank=True,
                                                      null=True)
    monterrey_cti_mayo_comentarios = models.CharField(max_length=200, verbose_name="MONTERREY CTI MAYO ", blank=True,
                                                      null=True)
    tlane_cti_vallejo_comentarios = models.CharField(max_length=200, verbose_name="TLANE CTI VALLEJO ", blank=True,
                                                     null=True)
    tijuana_otay_comentarios = models.CharField(max_length=200, verbose_name="TIJUANA OTAY", blank=True, null=True)
    monterrey_cti_revolucion_comentarios = models.CharField(max_length=200, verbose_name="MONTERREY CTI REVOLUCION ",
                                                            blank=True, null=True)
    tlaquepaque_sbcq21pre_gdl_comentarios = models.CharField(max_length=200, verbose_name="TLAQUEPAQUE_SBCQ21PRE_GDL",
                                                             blank=True, null=True)
    apodaca_sbcq21mty_mty_comentarios = models.CharField(max_length=200, verbose_name="APODACA_SBCQ21MTY_MTY",
                                                         blank=True, null=True)
    megacentro_sbcq21pre_cdmx_comentarios = models.CharField(max_length=200, verbose_name="MEGACENTRO_SBCQ21PRE_CDMX",
                                                             blank=True, null=True)
    sbcq21mty_apodaca_comentarios = models.CharField(max_length=200, verbose_name="SBCQ21MTY_APODACA", blank=True,
                                                     null=True)
    sbg_ericcson_leo_tlaquepaque_comentarios = models.CharField(max_length=200,
                                                                verbose_name="SBG_ERICCSON LEO_TLAQUEPAQUE", blank=True,
                                                                null=True)
    sbg_ericcson_gdl_megacentro_comentarios = models.CharField(max_length=200,
                                                               verbose_name="SBG_ERICCSON GDL_MEGACENTRO", blank=True,
                                                               null=True)
    presa_sae_2884_comentarios = models.CharField(max_length=200, verbose_name="PRESA SAE-2884", blank=True, null=True)
    gdl_sae_2876_comentarios = models.CharField(max_length=200, verbose_name="GDL SAE-2876", blank=True, null=True)
    mty_sae_2885_comentarios = models.CharField(max_length=200, verbose_name="MTY SAE-2885", blank=True, null=True)
    dfp_tcl_in_vallejo_comentarios = models.CharField(max_length=200, verbose_name="DFP_TCL_IN_VALLEJO", blank=True,
                                                      null=True)
    dfn_tcl_in_nextengo_comentarios = models.CharField(max_length=200, verbose_name="DFN_TCL_IN_NEXTENGO", blank=True,
                                                       null=True)
    mty_tcl_in_sanpedro_comentarios = models.CharField(max_length=200, verbose_name="MTY_TCL_IN_SANPEDRO", blank=True,
                                                       null=True)
    mtp_tcl_in_revolucion_comentarios = models.CharField(max_length=200, verbose_name="MTP_TCL_IN_REVOLUCION",
                                                         blank=True, null=True)
    gdl_tcl_in_bandera_comentarios = models.CharField(max_length=200, verbose_name="GDL_TCL_IN_BANDERA", blank=True,
                                                      null=True)
    gdl_tcl_in_tlaquepaque_comentarios = models.CharField(max_length=200, verbose_name="GDL_TCL_IN_TLAQUEPAQUE",
                                                          blank=True, null=True)
    pue_tcl_in_fuertes_comentarios = models.CharField(max_length=200, verbose_name="PUE_TCL_IN_FUERTES", blank=True,
                                                      null=True)
    pue_tcl_in_ctp_comentarios = models.CharField(max_length=200, verbose_name="PUE_TCL_IN_CTP", blank=True, null=True)
    gdl_sip_bandera_comentarios = models.CharField(max_length=200, verbose_name="GDL SIP BANDERA ", blank=True,
                                                   null=True)
    mty_sip_san_pedro_comentarios = models.CharField(max_length=200, verbose_name="MTY SIP SAN PEDRO", blank=True,
                                                     null=True)
    tln_sip_nextengo_comentarios = models.CharField(max_length=200, verbose_name="TLN SIP NEXTENGO  ", blank=True,
                                                    null=True)
    icx_marcatel_gdl_comentarios = models.CharField(max_length=200, verbose_name="ICX_MARCATEL_GDL", blank=True,
                                                    null=True)
    mty_icx_vsbgmty_comentarios = models.CharField(max_length=200, verbose_name="MTY_ICX_VSBGMTY  ", blank=True,
                                                   null=True)
    altan_vsbg2_mty_comentarios = models.CharField(max_length=200, verbose_name="ALTAN_vSBG2_MTY", blank=True,
                                                   null=True)
    altan_vsbg2_tlane_comentarios = models.CharField(max_length=200, verbose_name="ALTAN_vSBG2_TLANE", blank=True,
                                                     null=True)


    class Meta:
        verbose_name = "Comentarios de Rutas Interconexión"
        verbose_name_plural = "Health Check Comentarios de Rutas de Interconexión"


class RutasInterFolioGuio(models.Model):
    puebla_cti_fuertes_folios_IN = models.CharField(max_length=200, verbose_name=" IN PUEBLA CTI FUERTES ", blank=True,
                                                    null=True)
    tijuana_cti_pio_pico_folios_IN = models.CharField(max_length=200, verbose_name=" IN TIJUANA CTI PIO PICO ",
                                                      blank=True, null=True)
    presa_cti_nextengo_folios_IN = models.CharField(max_length=200, verbose_name=" IN PRESA CTI NEXTENGO ", blank=True,
                                                    null=True)
    guadalajara_cti_tlaquepaque_folios_IN = models.CharField(max_length=200,
                                                             verbose_name=" IN GUADALAJARA CTI TLAQUEPAQUE", blank=True,
                                                             null=True)
    monterrey_cti_mayo_folios_IN = models.CharField(max_length=200, verbose_name=" IN MONTERREY CTI MAYO ", blank=True,
                                                    null=True)
    monterrey_cti_revolucion_folios_IN = models.CharField(max_length=200, verbose_name=" IN MONTERREY CTI REVOLUCION ",
                                                          blank=True, null=True)
    tlane_cti_vallejo_folios_IN = models.CharField(max_length=200, verbose_name=" IN TLANE CTI VALLEJO ", blank=True,
                                                   null=True)
    presa_cti_nextengo_folios = models.CharField(max_length=200, verbose_name="PRESA CTI NEXTENGO ", blank=True,
                                                 null=True)
    monterrey_cti_mayo_folios = models.CharField(max_length=200, verbose_name="MONTERREY CTI MAYO ", blank=True,
                                                 null=True)
    tlane_cti_vallejo_folios = models.CharField(max_length=200, verbose_name="TLANE CTI VALLEJO ", blank=True,
                                                null=True)
    tijuana_otay_folios = models.CharField(max_length=200, verbose_name="TIJUANA OTAY", blank=True, null=True)
    monterrey_cti_revolucion_folios = models.CharField(max_length=200, verbose_name="MONTERREY CTI REVOLUCION ",
                                                       blank=True, null=True)
    tlaquepaque_sbcq21pre_gdl_folios = models.CharField(max_length=200, verbose_name="TLAQUEPAQUE_SBCQ21PRE_GDL",
                                                        blank=True, null=True)
    apodaca_sbcq21mty_mty_folios = models.CharField(max_length=200, verbose_name="APODACA_SBCQ21MTY_MTY", blank=True,
                                                    null=True)
    megacentro_sbcq21pre_cdmx_folios = models.CharField(max_length=200, verbose_name="MEGACENTRO_SBCQ21PRE_CDMX",
                                                        blank=True, null=True)
    sbcq21mty_apodaca_folios = models.CharField(max_length=200, verbose_name="SBCQ21MTY_APODACA", blank=True, null=True)
    sbg_ericcson_leo_tlaquepaque_folios = models.CharField(max_length=200, verbose_name="SBG_ERICCSON LEO_TLAQUEPAQUE",
                                                           blank=True, null=True)
    sbg_ericcson_gdl_megacentro_folios = models.CharField(max_length=200, verbose_name="SBG_ERICCSON GDL_MEGACENTRO",
                                                          blank=True, null=True)
    presa_sae_2884_folios = models.CharField(max_length=200, verbose_name="PRESA SAE-2884", blank=True, null=True)
    gdl_sae_2876_folios = models.CharField(max_length=200, verbose_name="GDL SAE-2876", blank=True, null=True)
    mty_sae_2885_folios = models.CharField(max_length=200, verbose_name="MTY SAE-2885", blank=True, null=True)
    dfp_tcl_in_vallejo_folios = models.CharField(max_length=200, verbose_name="DFP_TCL_IN_VALLEJO", blank=True,
                                                 null=True)
    dfn_tcl_in_nextengo_folios = models.CharField(max_length=200, verbose_name="DFN_TCL_IN_NEXTENGO", blank=True,
                                                  null=True)
    mty_tcl_in_sanpedro_folios = models.CharField(max_length=200, verbose_name="MTY_TCL_IN_SANPEDRO", blank=True,
                                                  null=True)
    mtp_tcl_in_revolucion_folios = models.CharField(max_length=200, verbose_name="MTP_TCL_IN_REVOLUCION", blank=True,
                                                    null=True)
    gdl_tcl_in_bandera_folios = models.CharField(max_length=200, verbose_name="GDL_TCL_IN_BANDERA", blank=True,
                                                 null=True)
    gdl_tcl_in_tlaquepaque_folios = models.CharField(max_length=200, verbose_name="GDL_TCL_IN_TLAQUEPAQUE", blank=True,
                                                     null=True)
    pue_tcl_in_fuertes_folios = models.CharField(max_length=200, verbose_name="PUE_TCL_IN_FUERTES", blank=True,
                                                 null=True)
    pue_tcl_in_ctp_folios = models.CharField(max_length=200, verbose_name="PUE_TCL_IN_CTP", blank=True, null=True)
    gdl_sip_bandera_folios = models.CharField(max_length=200, verbose_name="GDL SIP BANDERA ", blank=True, null=True)
    mty_sip_san_pedro_folios = models.CharField(max_length=200, verbose_name="MTY SIP SAN PEDRO", blank=True, null=True)
    tln_sip_nextengo_folios = models.CharField(max_length=200, verbose_name="TLN SIP NEXTENGO  ", blank=True, null=True)
    icx_marcatel_gdl_folios = models.CharField(max_length=200, verbose_name="ICX_MARCATEL_GDL", blank=True, null=True)
    mty_icx_vsbgmty_folios = models.CharField(max_length=200, verbose_name="MTY_ICX_VSBGMTY  ", blank=True, null=True)
    altan_vsbg2_mty_folios = models.CharField(max_length=200, verbose_name="ALTAN_vSBG2_MTY", blank=True, null=True)
    altan_vsbg2_tlane_folios = models.CharField(max_length=200, verbose_name="ALTAN_vSBG2_TLANE", blank=True, null=True)

    class Meta:
        verbose_name = "Folios Guios de Rutas Interconexión"
        verbose_name_plural = "Health Check Folios Guios de Rutas de Interconexión"
    
class HcAPN(models.Model):
    apn_mvn0_helppy_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 HELPPY STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_helppy_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 HELPPY COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_helppy_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 HELPPY FOLIOS", 
                                            blank=True, null=True)
    
    
    apn_mvn0_tokamovil_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 TOKAMOVIL STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_tokamovil_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 TOKAMOVIL COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_tokamovil_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 TOKAMOVIL FOLIOS", 
                                            blank=True, null=True)
    
    
    apn_mvn0_simpati_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 simpati STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_simpati_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 simpati COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_simpati_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 simpati FOLIOS", 
                                            blank=True, null=True)


    apn_mvn0_flashmobile_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 flashmobile STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_flashmobile_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 flashmobile COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_flashmobile_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 flashmobile FOLIOS", 
                                            blank=True, null=True)


    apn_mvn0_hermobile_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 HERMOBILE STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_hermobile_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 HERMOBILE COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_hermobile_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 HERMOBILE FOLIOS", 
                                            blank=True, null=True)


    apn_mvn0_weex_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 WEEX STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_weex_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 WEEX COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_weex_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 WEEX FOLIOS", 
                                            blank=True, null=True)

    
    apn_mvn0_movistar_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 MOVISTAR STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_movistar_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 MOVISTAR COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_movistar_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 MOVISTAR FOLIOS", 
                                            blank=True, null=True) 


    apn_mvn0_virgin_mobile_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 VIRGIN MOBILE STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_virgin_mobile_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 VIRGIN MOBILE COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_virgin_mobile_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 VIRGIN MOBILE FOLIOS", 
                                            blank=True, null=True) 


    apn_mvn0_six_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 SIX STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_six_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 SIX COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_six_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 SIX FOLIOS", 
                                            blank=True, null=True)


    apn_mvn0_internet_fijo_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="APN-MVN0 INTERNET FIJO STATUS",
                                            blank=True, null=True, default='OK')
    
    apn_mvn0_internet_fijo_comentarios = models.CharField(max_length=200,
                                                verbose_name="APN-MVN0 INTERNET FIJO COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    apn_mvn0_internet_fijo_folios = models.CharField(max_length=200, 
                                            verbose_name="APN-MVN0 INTERNET FIJO FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_telcel_2852_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel 2852 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_2852_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel 2852 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_2852_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel 2852 FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_telcel_305_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel 305 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_305_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel 305 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_305_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel 305 FOLIOS", 
                                            blank=True, null=True)      


    grx_roaming_telcel_301_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel 301 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_301_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel 301 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_301_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel 301 FOLIOS", 
                                            blank=True, null=True)     


    grx_roaming_telcel_2851_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel 2851 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_2851_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel 2851 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_2851_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel 2851 FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_telcel_interconexión_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel Interconexión STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_interconexión_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel Interconexión COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_interconexión_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel Interconexión FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_telcel_212_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel 212 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_212_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel 212 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_212_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel 212 FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_telcel_entrante_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel ENTRANTE STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_entrante_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel ENTRANTE COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_entrante_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel ENTRANTE FOLIOS", 
                                            blank=True, null=True)

    
    grx_roaming_telcel_suma_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Telcel SUMA STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_telcel_suma_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Telcel SUMA COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_telcel_suma_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Telcel SUMA FOLIOS", 
                                            blank=True, null=True)


    grx_roaming_nextel_tlalnemty_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Nextel TLALNE + MTY STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_nextel_tlalnemty_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Nextel TLALNE + MTY COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_nextel_tlalnemty_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Nextel TLALNE + MTY FOLIOS", 
                                            blank=True, null=True)                                                                                                                                           


    grx_roaming_altan_tln_vlan_355_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Altan TLN VLAN 355 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_altan_tln_vlan_355_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Altan TLN VLAN 355 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_altan_tln_vlan_355_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Altan TLN VLAN 355 FOLIOS", 
                                            blank=True, null=True)        


    grx_roaming_altan_mty_vlan_355_status = models.CharField(choices=ESTATUS, max_length=45,
                                            verbose_name="GRX Roaming Altan MTY VLAN 355 STATUS",
                                            blank=True, null=True, default='OK')
    
    grx_roaming_altan_mty_vlan_355_comentarios = models.CharField(max_length=200,
                                                verbose_name="GRX Roaming Altan MTY VLAN 355 COMENTARIOS",
                                                blank=True, null=True, default='TRAFICO ESTABLE')
    
    grx_roaming_altan_mty_vlan_355_folios = models.CharField(max_length=200, 
                                            verbose_name="GRX Roaming Altan MTY VLAN 355 FOLIOS", 
                                            blank=True, null=True)                                              