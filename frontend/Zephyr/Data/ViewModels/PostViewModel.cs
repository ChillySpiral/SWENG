namespace Zephyr.Data.ViewModels
{
    public class PostViewModel
    {
        // ToDo: Remove Test Image
        private string _imageStringBase64 =
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEQ0lEQVR4XsVWTWxMURQ+XgaqagiFRkwjQcRCoxIrdKkJDFY0RRdUbEotREOMaFiAsWtZgEAkpEGiK6YsqZBIRRFGiqCio+0U8Jzv5n7JzctkzDTwJSd59+fdc853fu4d4vu+/E+E5B9hYGCgVAcnVXpU4gUFBQnMe39JWVQlprLFmY6rLFJZrnKTawjBn1a+XgcnnKkalTEqRzBo2vNeNu0uxmdKpdT7kxSrtFD53UQ/l2BQDINLxz7K7Wu98qh9AMOwSjSUR/wgFZIZZZZaSff+lNOHP0j3628yr6JQLO2S7Pwql49/FKDtWp/MKi+QbAZAKWjbYj2ISA64pd7By+4332XlhrECUHlj7WshwAANz2gAEsTSFqZXyc4v5qB+/SZcBTg03cc1kYVLiwRoPZ+CUe6aMdAiEgp6bbN1HS29fv6TtLf1Sz6YNXeE+bfRshEEnRpZ5LEKhAYkEDMsIltdxSNHeRKZMcz1ml4NCvvOTjHnhRzlcSrfq/F6+eSrAOWLCqVy9WgmDcFYGnof3fss+YLOeFY5srvOVQ6Ptx6YKPUHJ8r4kqFy5tAHJBLFjIGdzSXYh/2Db8W2RWq8U1DOg2GlUdR6ISVBwGvMgyE0FuxvqOrKOUcs2jzrfeS9JgvrtLp+HJTDU6MkG5AnYK14csj8lwPccN73bJ3Lrau9AozXgxavDjO2nDM0n70zjSLHb5TK1OkmjmAN+/Gf2fsbsEEBCY/dja2zUpUjF1C/VL4fGTtzuFFCuaue71LaqRBMgUX8/xv6mYApvRFb8HeEXpCeDqeprNo4Vvr1u2FNF+d4kCxcUmSoZ623qxM4PBvAkpt3HpuCWx6ocQJKEJ4cah5dEg5k8570g944DTDU/W2gTGtjEzjEg+QFDSBtQmOKS0ICMDfQ14N1Tk/RIwj8RzaDqNVSRbgUD1R5jPOeayG7Gw/nHV6oa6hz1DxoxGHIDYRqrZZetRWEC70kk3JSz6ojJJ1OJ1T8xs3P/RWzH/oN1U99jA9vT2JspC7a6SeffcK8ke63fWa9an6H33rxLef8M/FX2E9x1yE9KmW4e1wZopO4eo/gLm/WCwjY2TRZwzJcdlR1McNZkmCKFZMV6BGbNOYsOZS7Un9fCCcELcx2KOC7Dag/OAkHufd4VuU0EpTvPzeFMQd6qDwIz2bjKRX0dCpie0WzwesGB2dVukAdQLc8emWqzNNcwR2CZmUxxrw1guCr2C7CkDBDwcSs3maSixWCt17GauAbAUmIhsT/LFag60kQrAJd7LEtOQVloBBA84ExdcteGo+Sj78I4VZJk92jtyH2oGKgnLGvofJMCL6IorZFhuFtc+wdL6Sckq5yTdj1OqkSZexzMYBGlFkj5pB2UNrR/lmbzA8h2IRKNcvLKwqZcMQelbhlVvIxIPgyhkQkNyRhOIRtFhisAQSfa5QgoAgUJ4JU52XA/8QvRgye1rf4g4QAAAAASUVORK5CYII=";

        public int Id { get; set; }
        public string? Text { get; set; }

        public string? ImageUrl
        {
            get => _imageStringBase64;
            set => _imageStringBase64 = value;
        }
        public UserViewModel User { get; set; }
    }
}
