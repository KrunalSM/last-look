create table public.profiles (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  password_hash text not null,
  marketing_opt_in boolean not null default false,
  created_at timestamptz not null default now()
);

alter table public.profiles disable row level security;
