﻿using Zephyr.Data.ViewModels;

namespace Zephyr.Data
{
    public interface IBusinessLayer
    {
        public List<PostViewModel> GetAllPosts();
    }
}