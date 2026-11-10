create table public.profiles (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  password_hash text not null,
  marketing_opt_in boolean not null default false,
  marketing_opt_in_at timestamptz,
  privacy_version text not null,
  terms_version text not null,
  terms_accepted_at timestamptz not null,
  created_at timestamptz not null default now()
);

alter table public.profiles enable row level security;
create policy "own row" on public.profiles for select using (auth.uid() = id);

create table public.content_reports (
  id bigint generated always as identity primary key,
  url text not null,
  reason text not null,
  created_at timestamptz not null default now()
);

alter table public.content_reports enable row level security;
