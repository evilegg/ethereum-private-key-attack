"""Cache of target ETH address we are trying to crack."""

import yaml


def targets(stream=None):
    """Load targets from a yaml stream (or return default)."""
    if stream:
        return yaml.safe_load(stream)
    else:
        # return a hardcoded copy of top-100 addresses
        return [
            '0000000000000000000000000000000000000000',
            '000000000000000000000000000000000000dead',
            '000009d8131fa90e85b48a901c9a3df30fe63f89',
            '0001120c65e60078fef36fe278aad3aa2cddb172',
            '00013b0ac844c32833642f67be2d585f3fb7aaa0',
            '00018b5e3d3c2f43c1e2ccb15f7b7332b312623e',
            '0001ab7ad20264ea13b3b87c5a80f640748399fb',
            '0001b49181639d5ba5105cd96fce780cb73fda4f',
            '0001f74eb4854f9ee81564b6343d612c2c5a691a',
            '0001fd043311c5942e0e0b11b8e9634f35f73fad',
            '0002fa49043113ec2b40092c3873e1125cf89bbf',
            '00055ad45e27bfa929c3efb6bdca59e83812a2b7',
            '00056f463017c7be5ed5223c2930c3086a779586',
            '0006f944e0f0d868848ac51502ecd301dfb63b4f',
            '00073103c819211ef56d0a8ba7f71c11a84aa55f',
            '0007a3f6a0dc83c299f1076bbfc2799fe940c0b9',
            '000901c9bafb0b2094c9d23cdf792a88d5839a82',
            '00099dc7dd85213f5f10dd1f7033b72f552ae58d',
            '000a1c9145b73cf46993fd810ab6773135742896',
            '000a89419ba4ea71aa57b5b5562405799069571d',
            '000d6883608019dc3c169fa0e7801f4514645f15',
            '000e0e5701b14fb77160bcc7bfe7256522d5927b',
            '000f372e3e45ada03456aef3b90c545ff2b7329c',
            '000f8ef81ef1415a425091fd80215c5b8dfec563',
            '001101c04e5125d18f2d57269c4dbde5511b7ac7',
            '00128d2f78b22a11ce4b1fd7eb8cfa3f7b788d66',
            '0012aa4453c184a2e43f3876abf9cc38254d029c',
            '001583b146b426376d166e8af3f65bd2b6f36f21',
            '0015f63460ec7ab5ec6e83b74aca422532d2cbee',
            '0016ce6ff889307ee088a9c288215350035681d8',
            '001866ae5b3de6caa5a51543fd9fb64f524f5478',
            '0019142ea15d5e963a4b75ac72a6f64b344a8abb',
            '0019312d39a13302fbacedf995f702f6e071d9e8',
            '001de0ab13c480e6d0f47e6d275c8afcdce2ce78',
            '001e189650980cc56d1b67122a3a30779ba3a6fb',
            '001e7bbf4079d3bfd2089fca211df596a8d5c30b',
            '001ea4060eef514f681d5280e52edea589bfc6d1',
            '001ecaf34c88a5fcfc455242e832d671a3bd739f',
            '00213f9ce9e1787336926bf094488086763079ac',
            '0022003b60e97196c0a341566126d35eb4d7e402',
            '00225c538542ef196ad0273374c13f73a1adca84',
            '00233eddd6a632aad3cf1f3bd268d00b5bb4d70d',
            '0025ca5a6090b729bdb71b7ce1fddd0e460b7703',
            '0026eb9da02470e57b4d0ed8b312b39443d6d29e',
            '0027912f8b96e9dfab6342d36af020e0282a1407',
            '00294facdb03e5422deeea8858cc8dcfe7ec6225',
            '002d27082129124544148246a221366cd71844f2',
            '00311c3e2d2e60fe50df22aca488b170b6cad337',
            '00316d956f5f35591ae021f4858a2a865c6ba02a',
            '0032ba9b8720ee48030071f0947b285d2d9ccfa1',
            '0034cf6e02f4c47fb30df22fc81b8dedddbf1fb0',
            '00359d862dd26307b0816f7ba3501a01808706fa',
            '0036289f041537bd953e5ca57ec3ec530dce2153',
            '0036671aadc726b80b3c6e5ee9d2b60367d6f10e',
            '00378fc6963702ede7c05d38cca7718fdbdba709',
            '003873ce9607827bc820ea1818a0b8d5436f661c',
            '003a4cc04501e9adecf850313db2d3797df801a2',
            '003a6b96105069e5eac52921abf147cde0822544',
            '003b17a52f2ecd363488b9c85ff7912e6e804c0e',
            '003bde955a7c56487da95c3f8497966b478e2390',
            '003ca46abf60d34479f1cfafa1ffe25853aa68c9',
            '003cc9f2ce96666fcc2127b94e596b93e7798ef9',
            '003e93083a2d294cb8c4421048108330c37b5874',
            '003f01a677440f4df2b94c86d235b9fdaea34921',
            '0040f2b793ac6db66634f96cb81863ad5cc1dced',
            '0041179685dcbfdce65e4a3bf6852ea9fe878b78',
            '0041e3db2b27d16a2f4fd5f6a5622974fff104dd',
            '0046576d15a1d5cbf83eca1353e8197407429b10',
            '004a28d65e7123cc48360ea69abcc527301c826a',
            '004a74fb3d04cd3314a02a72a09bc09ce4460be5',
            '004cfb59553b5d5e78bad38ebbb506f44ed53992',
            '004e0de965f34f651e66bebfbc2be279cea130e6',
            '004e3def0c754a921af751d1004df95f9650ea00',
            '004ef7d107051c83f8a1db61c6ef2a80c4230cd1',
            '005097fa238b15c53ad0ba38edf60177fd28cbde',
            '00527a2b537a07d6ccfe8150a0bfe5e2ea15f172',
            '0053e10ec86fb22296ce29a03d446776fec2a7c4',
            '0055c95f8273f59401391baff9faf370d869984c',
            '00560dd02c47c2a1e2042b0b0c0ca4d05363f725',
            '00564752dfe1ba52efcd6478e16dfbe21e2a7d11',
            '0056d9b61deab6a7f0cc8e9f5c63879d373b24e1',
            '005a8d02a46ea53530e6d0cd8600e04c09c90e00',
            '0060de2860115de9eb43ce872c5e71a6785d248e',
            '0062ae9e75f188642212f279c041226d8f45a829',
            '006bb362c27df2e55bea1066e65e9c55f072e354',
            '0070159d4e20ad35e19585e780ce9b37ccdcf6cd',
            '00718966b4d025db298816ddda7189f62a095177',
            '007199080eb1bd77e06212b469f6f1fd60234744',
            '0073c423a0b5d88b330d481301025db1ab65d891',
            '0073def4e522db78c4080f8fed03d6b8185ae819',
            '00744245df4deeb3d17a6bbe4605d55a2244c5cb',
            '0077a93f7a3729d8a342d16a61c47890fe3f3576',
            '00791803ce12bca730f8e3f29f0c6aee29f0c19d',
            '0079418d9dc201b95717806441698a949adb8fee',
            '007a8d1d6550b2254e5d0e6edbb5f4d159928320',
            '007b9fc31905b4994b04c9e2cfdc5e2770503f42',
            '007bf5b1a3ff72cd50dade030899efec8087addd',
            '0080b1007a72e1a000a8d3a3f47d27498183d35d',
            '008173fd32d84281cc9c614acb96b24acac85979',
            '008279d03770830f597a381a1760095508acd174',
        ]
