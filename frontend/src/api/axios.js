import axios from 'axios';
import {QueryClient, useMutation, useQuery} from '@tanstack/react-query';

export const BaseURL = process.env.REACT_APP_BASE_URL;
const timeout = 1000 * 10;

export const api = axios.create({
  baseURL: BaseURL,
  headers: {
    'Content-Type': 'application/json',
    accept: '*/*',
  },
  timeout: timeout,
});

export const ErrorTypes = {
  BadRequest: 'BAD_REQUEST',
  EntityNotFoundException: 'EntityNotFoundException',
};

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: false,
    },
  },
})


export const useService = () => {
  const useGet = (key, path, enabled) => {
    return useQuery({
      queryKey: [key],
      queryFn: () => {
        return api.get(path);
      },
      enabled: enabled || false,
    });
  };

  const useGetTable = (key, path, tableConfig) => {
    return useQuery({
      queryKey: [key],
      queryFn: () => {
        return api.post(path, tableConfig);
      },
    });
  };

  const usePost = (key, path) => {
    return useMutation({
      mutationKey: [key],
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: [key],
        });
      },
      mutationFn: (data) => {
        return api.post(path, data);
      },
    });
  };

  const useDelete = (key, path) => {
    return useMutation({
      mutationKey: [key],
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: [key],
        });
      },
      mutationFn: () => {
        return api.delete(path);
      },
    });
  };

  const usePut = (key, path) => {
    return useMutation({
      mutationKey: [key],
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: [key],
        });
      },
      mutationFn: (data) => {
        return api.put(path, data);
      },
    });
  };

  return {
    usePost,
    useDelete,
    useGetTable,
    usePut,
    useGet,
  };
};